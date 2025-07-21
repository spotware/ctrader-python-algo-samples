import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class LinearRegressionRSquaredSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.linearRegressionRSquared = api.Indicators.LinearRegressionRSquared(api.SourceLinearRegression, api.PeriodsLinearRegression);
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(self.linearRegressionRSquared.Result, api.PeriodsSimpleMovingAverage);
        self.exponentialMovingAverage = api.Indicators.ExponentialMovingAverage(api.SourceExponentialMovingAverage, api.PeriodsExponentialMovingAverage);

    def on_bar_closed(self):
        if api.Bars.ClosePrices.Last(0) > self.exponentialMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) <= self.exponentialMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Sell)
            if self.linearRegressionRSquared.Result.Last(0) > self.simpleMovingAverage.Result.Last(0):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.exponentialMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) >= self.exponentialMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Buy)
            if self.linearRegressionRSquared.Result.Last(0) > self.simpleMovingAverage.Result.Last(0):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)