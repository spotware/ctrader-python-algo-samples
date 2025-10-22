import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleDeMarker():
    def initialize(self):
        self.deMin = api.CreateDataSeries()
        self.deMax = api.CreateDataSeries()
        self.deMinMA = api.Indicators.MovingAverage(self.deMin, api.Periods, MovingAverageType.Simple)
        self.deMaxMA = api.Indicators.MovingAverage(self.deMax, api.Periods, MovingAverageType.Simple)
        
    def calculate(self, index):
        self.deMin[index] = max(api.Bars.LowPrices[index - 1] - api.Bars.LowPrices[index], 0)
        self.deMax[index] = max(api.Bars.HighPrices[index] - api.Bars.HighPrices[index - 1], 0)

        minValue = self.deMinMA.Result[index]
        maxValue = self.deMaxMA.Result[index]

        api.DMark[index] = maxValue / (minValue + maxValue)