import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class CyberCycleSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.cyberCycle  = api.Indicators.CyberCycle(api.Alpha)

    def on_bar_closed(self):
        if self.cyberCycle.Cycle.Last(0) > self.cyberCycle.Trigger.Last(0) and self.cyberCycle.Cycle.Last(1) <= self.cyberCycle.Trigger.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.cyberCycle.Cycle.Last(0) < self.cyberCycle.Trigger.Last(0) and self.cyberCycle.Cycle.Last(1) >= self.cyberCycle.Trigger.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)