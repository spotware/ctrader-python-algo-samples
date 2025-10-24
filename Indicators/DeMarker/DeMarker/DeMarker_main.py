import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class DeMarker():
    def initialize(self):
        self.deMax = api.CreateDataSeries()
        self.deMin = api.CreateDataSeries()
        
        self.deMaxSma = api.Indicators.SimpleMovingAverage(self.deMax, api.Periods)
        self.deMinSma = api.Indicators.SimpleMovingAverage(self.deMin, api.Periods)
        
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index < 1:
            api.Result[outputIndex] = float('nan')
            return

        self.deMax[index] = api.Bars.HighPrices[index] - api.Bars.HighPrices[index - 1] if api.Bars.HighPrices[index] > api.Bars.HighPrices[index - 1] else 0
        self.deMin[index] = api.Bars.LowPrices[index - 1] - api.Bars.LowPrices[index] if api.Bars.LowPrices[index] < api.Bars.LowPrices[index - 1] else 0

        if self.deMaxSma.Result[index] + self.deMinSma.Result[index] == 0:
            api.Result[outputIndex] = float('nan')
            return

        api.Result[outputIndex] = self.deMaxSma.Result[index] / (self.deMaxSma.Result[index] + self.deMinSma.Result[index])