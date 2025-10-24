import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CyberCycle():
    def initialize(self):
        self.medianPriceDataSeries = api.Indicators.MedianPrice().Result
        self.smoothDataSeries = api.CreateDataSeries()
        
    def calculate(self, index):
        self.smoothDataSeries[index] = (self.medianPriceDataSeries[index] + 2 * self.medianPriceDataSeries[index - 1] + 2 * self.medianPriceDataSeries[index - 2] + self.medianPriceDataSeries[index - 3]) / 6

        api.Cycle[index] = (1 - 0.5 * api.Alpha) * (1 - 0.5 * api.Alpha) * (self.smoothDataSeries[index] - 2 * self.smoothDataSeries[index - 1] + self.smoothDataSeries[index - 2]) + 2 * (1 - api.Alpha) * api.Cycle[index - 1] - (1 - api.Alpha) * (1 - api.Alpha) * api.Cycle[index - 2]

        if index < 7:
            api.Cycle[index] = (self.medianPriceDataSeries[index] - 2 * self.medianPriceDataSeries[index - 1] + self.medianPriceDataSeries[index - 2]) / 4

        api.Trigger[index] = api.Cycle[index - 1]