import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class VerticalHorizontalFilterSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.verticalHorizontalFilter = api.Indicators.VerticalHorizontalFilter(api.Source, api.Periods)
        self.verticalHorizontalFilterSimpleMovingAverage = api.Indicators.SimpleMovingAverage(self.verticalHorizontalFilter.Result, 14)
        self.priceSimpleMovingAverage = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 14)

    def on_bar_closed(self):
        if self.verticalHorizontalFilter.Result.Last(0) < self.verticalHorizontalFilterSimpleMovingAverage.Result.Last(1):
            return

        if api.Bars.ClosePrices.Last(0) > self.priceSimpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) <= self.priceSimpleMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.priceSimpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) >= self.priceSimpleMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)