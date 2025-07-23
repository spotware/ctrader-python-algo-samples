import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class VolumeIndexSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.positiveVolumeIndex = api.Indicators.PositiveVolumeIndex(api.PositiveSource)
        self.negativeVolumeIndex = api.Indicators.NegativeVolumeIndex(api.NegativeSource)
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.SourceSimpleMovingAverage, api.PeriodSimpleMovingAverage)

    def on_bar_closed(self):
        if api.Bars.ClosePrices.Last(0) > self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Sell)
            if len(self.get_bot_positions()) == 0 and self.negativeVolumeIndex.Result.Last(0) > self.positiveVolumeIndex.Result.Last(0):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Buy)
            if len(self.get_bot_positions()) == 0 and self.negativeVolumeIndex.Result.Last(0) < self.positiveVolumeIndex.Result.Last(0):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)