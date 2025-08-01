import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IndicatorDataSeriesSample():
    def initialize(self):
        self.internalSeries = api.CreateDataSeries()

    def calculate(self, index):
        self.internalSeries[index] = api.Bars.HighPrices[index]
        api.Main[index] = self.internalSeries[index] - api.Bars.LowPrices[index]