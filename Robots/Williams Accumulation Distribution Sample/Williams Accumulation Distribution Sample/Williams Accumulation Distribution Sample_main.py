import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
import math

class WilliamsAccumulationDistributionSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.williamsAccumulationDistribution = api.Indicators.WilliamsAccumulationDistribution()
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.SourceMovingAverage, api.PeriodsMovingAverage)

    def on_bar_closed(self):
        correlation = self.get_correlation(14)

        if correlation > 0.85:
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

    def get_correlation(self, periods):
        x = [self.williamsAccumulationDistribution.Result[self.williamsAccumulationDistribution.Result.Count - v] for v in reversed(range(periods))]
        y = [api.Bars.ClosePrices[api.Bars.ClosePrices.Count - v] for v in reversed(range(periods))]

        if len(x) == 0 or len(y) == 0:
            return None

        xSum = sum(x)
        ySum = sum(y)

        xSumSquared = pow(xSum, 2)
        ySumSquared = pow(ySum, 2)

        xSquaredSum = sum([pow(v, 2) for v in x])
        ySquaredSum = sum([pow(v, 2) for v in y])

        xAndyProductSum = sum([x[i] * y[i] for i in range(len(x))])

        n = len(x)

        return (n * xAndyProductSum - xSum * ySum) / math.sqrt((n * xSquaredSum - xSumSquared) * (n * ySquaredSum - ySumSquared))