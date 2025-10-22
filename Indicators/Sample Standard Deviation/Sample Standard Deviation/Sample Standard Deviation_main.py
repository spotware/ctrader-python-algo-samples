import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class SampleStandardDeviation():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
    
    def calculate(self, index):
        average = self.movingAverage.Result[index]
        sumValue = 0

        for i in range(api.Periods):
            sumValue += pow(api.Source[index - i] - average, 2.0)

        api.Result[index] = math.sqrt(sumValue / api.Periods)