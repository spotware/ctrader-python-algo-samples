import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PartialCloseSample():
    def on_start(self):
        self.firstLevelCloseAmountInPercentage = api.FirstLevelCloseAmountInPercentage / 100
        self.secondLevelCloseAmountInPercentage = api.SecondLevelCloseAmountInPercentage / 100

        self.firstLevelClosedPositions = set()
        self.secondLevelClosedPositions = set()

        api.Positions.Opened += self.on_pos_opened
        api.Positions.Closed += self.on_pos_closed

    def on_pos_opened(self, args):
        # If there are other positions from same symbol then don't add the symbol Tick event handler
        # Because we already have one
        if len([pos for pos in api.Positions if pos.SymbolName == args.Position.SymbolName]) > 1:
            return

        # Add position symbol tick event handler
        positionSymbol = api.Symbols.GetSymbol(args.Position.SymbolName)
        positionSymbol.Tick += self.on_symbol_tick

    def on_pos_closed(self, args):
        # In case position closed fully clean it's enteries from ID collections
        if len([pos for pos in api.Positions if pos.Id == args.Position.Id]) == 0:
            if args.Position.Id in self.firstLevelClosedPositions:
                self.firstLevelClosedPositions.remove(args.Position.Id)
            if args.Position.Id in self.secondLevelClosedPositions:
                self.secondLevelClosedPositions.remove(args.Position.Id)

        # If there are other positions from same symbol then don't remove the symbol Tick event handler
        if len([pos for pos in api.Positions if pos.SymbolName == args.Position.SymbolName]) > 1:
            return

        # If there is no other position from the closed position symbol then remove the Tick event handler
        positionSymbol = api.Symbols.GetSymbol(args.Position.SymbolName)
        positionSymbol.Tick -= self.on_symbol_tick

    def on_symbol_tick(self, args):        
        symbolPositions = [pos for pos in api.Positions if pos.SymbolName == args.SymbolName]

        for position in symbolPositions:
            if position.Id not in self.firstLevelClosedPositions and position.Pips >= api.FirstLevelClosePips:
                self.close_position_by_volume_percenatage(position, self.firstLevelCloseAmountInPercentage)
                self.firstLevelClosedPositions.add(position.Id)
            elif position.Id not in self.secondLevelClosedPositions and position.Pips >= api.SecondLevelClosePips:
                self.close_position_by_volume_percenatage(position, self.secondLevelCloseAmountInPercentage)
                self.secondLevelClosedPositions.add(position.Id)
                
    def close_position_by_volume_percenatage(self, position, volumePercent):
        symbol = api.Symbols.GetSymbol(position.SymbolName)
        volumeToClose = symbol.NormalizeVolumeInUnits(position.VolumeInUnits * volumePercent, RoundingMode.ToNearest)
        api.ClosePosition(position, volumeToClose)