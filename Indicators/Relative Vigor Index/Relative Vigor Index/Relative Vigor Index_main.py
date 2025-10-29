import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class RelativeVigorIndex():
    def initialize(self):
        self.numerator = api.CreateDataSeries()
        self.denominator = api.CreateDataSeries()
        self.numeratorSma = api.Indicators.SimpleMovingAverage(self.numerator, api.Periods)
        self.denominatorSma = api.Indicators.SimpleMovingAverage(self.denominator, api.Periods)
        
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index < 3:
            api.Result[outputIndex] = float("nan")
            return

        a = api.Bars.ClosePrices[index] - api.Bars.OpenPrices[index]
        b = api.Bars.ClosePrices[index - 1] - api.Bars.OpenPrices[index - 1]
        c = api.Bars.ClosePrices[index - 2] - api.Bars.OpenPrices[index - 2]
        d = api.Bars.ClosePrices[index - 3] - api.Bars.OpenPrices[index - 3]
        
        self.numerator[index] = (a + 2 * b + 2 * c + d) / 6

        e = api.Bars.HighPrices[index] - api.Bars.LowPrices[index]
        f = api.Bars.HighPrices[index - 1] - api.Bars.LowPrices[index - 1]
        g = api.Bars.HighPrices[index - 2] - api.Bars.LowPrices[index - 2]
        h = api.Bars.HighPrices[index - 3] - api.Bars.LowPrices[index - 3]
        
        self.denominator[index] = (e + 2 * f + 2 * g + h) / 6

        if self.denominatorSma.Result[index] == 0 or math.isnan(self.denominatorSma.Result[index]):
            api.Result[outputIndex] = float("nan")
            return

        api.Result[outputIndex] = self.numeratorSma.Result[index] / self.denominatorSma.Result[index]
        api.Signal[outputIndex] = (api.Result[outputIndex] + 2 * api.Result[outputIndex - 1] + 2 * api.Result[outputIndex - 2] + api.Result[outputIndex - 3]) / 6