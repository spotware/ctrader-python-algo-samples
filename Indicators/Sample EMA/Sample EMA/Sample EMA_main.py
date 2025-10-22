import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class SampleEMA():
    def initialize(self):
        self.exp = 2.0 / (api.Periods + 1)

        
    def calculate(self, index):
        previousValue = api.Result[index - 1]

        if math.isnan(previousValue):
            api.Result[index] = api.Source[index]
        else:
            api.Result[index] = api.Source[index] * self.exp + previousValue * (1 - self.exp)