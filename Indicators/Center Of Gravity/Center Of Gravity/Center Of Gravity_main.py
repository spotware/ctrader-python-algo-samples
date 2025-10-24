import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CenterOfGravity():
    def initialize(self):
        self.medianPriceDataSeries = api.Indicators.MedianPrice().Result

    def calculate(self, index):
        if index < api.Length + 1:
            return

        numerator = 0
        denominator = 0

        for i in range(api.Length):
            numerator += (1 + i) * self.medianPriceDataSeries[index - i]
            denominator += self.medianPriceDataSeries[index - i]

        if denominator != 0:
            api.Result[index] = -numerator / denominator + (api.Length + 1) / 2

        api.Lag[index] = api.Result[index - 1]