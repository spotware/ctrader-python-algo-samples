import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WeightedMovingAverage():
    def initialize(self):
        self.weight = sum(range(1, api.Periods + 1))
        
    def calculate(self, index):
        total = 0.0
        j = index

        for period in reversed(range(api.Periods + 1)):
            total += period * api.Source[j]
            j -= 1

        api.Result[index + api.Shift] = total / self.weight