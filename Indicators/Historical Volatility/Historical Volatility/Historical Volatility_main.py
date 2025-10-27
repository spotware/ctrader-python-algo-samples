import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class HistoricalVolatility():
    def initialize(self):
        self.logarithms = api.CreateDataSeries()
        self.standardDeviation = api.Indicators.StandardDeviation(self.logarithms, api.Periods, MovingAverageType.Simple)
        
    def calculate(self, index):
        self.logarithms[index] = math.log10(api.Source[index] / api.Source[index - 1])
        api.Result[index] = self.standardDeviation.Result[index] * math.sqrt(api.BarHistory)