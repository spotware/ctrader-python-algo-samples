import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class WilliamsAccumulationDistribution():
    def calculate(self, index):
        trueRangeHigh = self.calculate_true_range_high(index)
        trueRangeLow = self.calculate_true_range_low(index)

        value = self.calculate_value(index, trueRangeLow, trueRangeHigh)

        previousValue = 0 if math.isnan(api.Result[index - 1]) else api.Result[index - 1]
        api.Result[index] = value + previousValue

    def calculate_true_range_high(self, index):
        trueHighRange = api.Bars.ClosePrices[index - 1]

        if api.Bars.HighPrices[index] > trueHighRange:
            trueHighRange = api.Bars.HighPrices[index]

        return trueHighRange

    def calculate_true_range_low(self, index):
        trueRangeLow = api.Bars.ClosePrices[index - 1]

        if api.Bars.LowPrices[index] < trueRangeLow:
            trueRangeLow = api.Bars.LowPrices[index]

        return trueRangeLow

    def calculate_value(self, index, trueRangeLow, trueHighRange):
        if api.Bars.ClosePrices[index] > api.Bars.ClosePrices[index - 1]:
            return api.Bars.ClosePrices[index] - trueRangeLow

        if api.Bars.ClosePrices[index] < api.Bars.ClosePrices[index - 1]:
            return api.Bars.ClosePrices[index] - trueHighRange

        return 0