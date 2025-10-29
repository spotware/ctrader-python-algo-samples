import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class StandardDeviation():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
        
    def calculate(self, index):
        sumValue = 0

        value = self.movingAverage.Result[index]

        for period in range(api.Periods):
            sumValue += pow(api.Source[index - period] - value, 2.0)

        api.Result[index] = math.sqrt(sumValue / api.Periods)