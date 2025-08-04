import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PlotTypeSample():
    def initialize(self):
        self.standardDeviation = api.Indicators.StandardDeviation(api.Bars.ClosePrices, 20, MovingAverageType.Simple)

    def calculate(self, index):
        api.DiscontinuousLine[index] = api.Bars.ClosePrices[index] + self.standardDeviation.Result[index]
        api.Histogram[index] = api.Bars.ClosePrices[index] + (self.standardDeviation.Result[index] * 1.5)
        api.Line[index] = api.Bars.ClosePrices[index] + (self.standardDeviation.Result[index] * 2)
        api.Points[index] = api.Bars.ClosePrices[index] + (self.standardDeviation.Result[index] * 2.5)