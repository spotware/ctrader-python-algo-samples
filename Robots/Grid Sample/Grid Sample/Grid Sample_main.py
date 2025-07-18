import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class GridSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.enoughMoney = True
        if len(self.get_grid_positions()) == 0:
            self.open_position()

    def on_tick(self):
        grid_positions = self.get_grid_positions()
        net_profit_sum = sum([p.NetProfit for p in grid_positions])
        if net_profit_sum >= api.TargetProfit:
            api.Print("Target profit is reached. Closing all grid positions")
            self.close_grid_positions()
            api.Print("All grid positions are closed. Stopping cBot")
            api.Stop()

        if len(grid_positions) > 0 and self.enoughMoney == True:
            position_with_highest_pips = sorted(grid_positions, key=lambda pos: pos.Pips, reverse=True)[0]
            distance = self.get_distance_in_pips(position_with_highest_pips)          
            if distance >= api.StepPips:
                self.open_position()
      
    def get_grid_positions(self):
        return [pos for pos in api.Positions if pos.SymbolName == api.SymbolName and pos.TradeType == api.TradeType]

    def open_position(self):
        result = api.ExecuteMarketOrder(api.TradeType, api.SymbolName, self.volumeInUnits, "Grid")
        if result.Error == ErrorCode.NoMoney:
            self.enoughMoney = False
            api.Print("Not enough money to open additional positions")

    def close_grid_positions(self):
        for position in self.get_grid_positions():
            position.Close()

        if len(self.get_grid_positions()) > 0:
            self.close_grid_positions()
    
    def get_distance_in_pips(self, position):
        return (position.EntryPrice - api.Symbol.Ask if position.TradeType == TradeType.Buy else api.Symbol.Bid - position.EntryPrice) / api.Symbol.PipSize