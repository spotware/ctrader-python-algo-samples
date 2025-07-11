import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class AlligatorSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.alligator = api.Indicators.Alligator(api.JawsPeriods, api.JawsShift, api.TeethPeriods, api.TeethShift, api.LipsPeriods, api.LipsShift)

    def on_bar_closed(self):
        if self.alligator.Lips.Last(0) > self.alligator.Teeth.Last(0) and self.alligator.Lips.Last(1) <= self.alligator.Teeth.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.alligator.Lips.Last(0) < self.alligator.Teeth.Last(0) and self.alligator.Lips.Last(1) >= self.alligator.Teeth.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)