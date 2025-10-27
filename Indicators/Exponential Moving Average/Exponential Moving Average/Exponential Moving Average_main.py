import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class ExponentialMovingAverage():
    def initialize(self):
        self.alpha = 2 / (api.Periods + 1)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        previousValue = api.Result[outputIndex - 1]

        if math.isnan(previousValue):
            api.Result[outputIndex] = api.Source[index]
        else:
            api.Result[outputIndex] = api.Source[index] * self.alpha + previousValue * (1 - self.alpha)