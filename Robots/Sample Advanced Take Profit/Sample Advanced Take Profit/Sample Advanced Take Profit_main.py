import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleAdvancedTakeProfit():
    def on_start(self):
        if api.PositionId is None or len(api.PositionId) == 0:
            self.print_error_and_stop("You have to specify \"Position Id\" in cBot Parameters")

        position = self.find_position_or_stop()
        
        self.symbolInfo = api.Symbols.GetSymbolInfo(position.SymbolName)

        self.levels = self.get_take_profit_levels()

        self.validate_levels(position)

    def on_tick(self):
        position = self.find_position_or_stop()
        reachedLevels = [l for l in self.levels if l.is_enabled and l.is_triggered == False and l.pips <= position.Pips]

        for reachedLevel in reachedLevels:
            reachedLevel.is_triggered = True

            api.Print(f"Level '{reachedLevel.name}' is reached. Level.Pips: {reachedLevel.pips}, Position.Pips: {position.Pips}, Position.Id: {position.Id}")
            
            volumeToClose = min(reachedLevel.volume, position.VolumeInUnits)

            result = api.ClosePosition(position, volumeToClose)

            if result.IsSuccessful == False:
                api.Print(f"Cannot close position, Id: {position.Id}, Error: {result}")

            remainingLevels = [l for l in self.levels if l.is_enabled and l.is_triggered == False]
            
            if len(remainingLevels) == 0:
                api.Print("All levels were reached. cBot is stopping...")
                api.Stop()
                break

    def print_error_and_stop(self, errorMessage):
        api.Print(errorMessage);
        api.Stop();

        raise Exception(errorMessage)

    def find_position_or_stop(self):
        positions = [p for p in api.Positions if f"PID{p.Id}" == api.PositionId or str(p.Id) == api.PositionId]
                
        if len(positions) == 0:
            self.print_error_and_stop(f"Position with Id = {api.PositionId} doesn't exist")

        return positions[0]

    def get_take_profit_levels(self):
        return [ 
            TakeProfitLevel("Take Profit 1", api.TakeProfit1Enabled, api.TakeProfit1Pips, api.TakeProfit1Volume),
            TakeProfitLevel("Take Profit 2", api.TakeProfit2Enabled, api.TakeProfit2Pips, api.TakeProfit2Volume),
            TakeProfitLevel("Take Profit 3", api.TakeProfit3Enabled, api.TakeProfit3Pips, api.TakeProfit3Volume)
        ]

    def validate_levels(self, position):
        self.make_sure_any_level_enabled()
        self.validate_total_volume(position)
        self.validate_reached_levels(position)
        self.validate_volumes()

    def make_sure_any_level_enabled(self):
        if len([l for l in self.levels if l.is_enabled]) == 0:
            self.print_error_and_stop("You have to enable at least one \"Take Profit\" in cBot Parameters")

    def validate_total_volume(self, position):
        totalVolume = sum([l.volume for l in self.levels if l.is_enabled])

        if totalVolume > position.VolumeInUnits:
            self.print_error_and_stop("The sum of all Take Profit respective volumes cannot be larger than the Position's volume")

    def validate_reached_levels(self, position):
        reachedLevels = [l for l in self.levels if l.pips <= position.Pips]

        if len(reachedLevels) > 0:
            self.print_error_and_stop(f"Level {reachedLevels[0].name} is already reached. The amount of Pips must be more than the amount of Pips that the Position is already gaining")

    def validate_volumes(self):
        enabledLevels = [l for l in self.levels if l.is_enabled]

        for level in enabledLevels:
            if level.volume < self.symbolInfo.VolumeInUnitsMin:
                self.print_error_and_stop(f"Volume for {self.symbolInfo.Name} cannot be less than {self.symbolInfo.VolumeInUnitsMin}")
            if level.volume > self.symbolInfo.VolumeInUnitsMax:
                self.print_error_and_stop(f"Volume for {self.symbolInfo.Name} cannot be greater than {self.symbolInfo.VolumeInUnitsMax}")
            if level.volume % self.symbolInfo.VolumeInUnitsMin != 0:
                self.print_error_and_stop(f"Volume {level.volume} is invalid")

class TakeProfitLevel():
    def __init__(self, name, is_enabled, pips, volume):
        self.name = name
        self.is_enabled = is_enabled
        self.pips = pips
        self.volume = volume
        self.is_triggered = False