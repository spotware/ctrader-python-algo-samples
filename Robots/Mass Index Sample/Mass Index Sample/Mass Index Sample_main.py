import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class MassIndexSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.massIndex = api.Indicators.MassIndex(api.Periods)
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.SourceSimpleMovingAverage, api.PeriodsSimpleMovingAverage)

    def on_bar_closed(self):
        if self.massIndex.Result.Last(0) < api.Periods:
            return

        if api.Bars.ClosePrices.Last(0) > self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)