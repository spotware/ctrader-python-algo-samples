import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class WellesWilderSmoothing():
    def calculate(self, index):
        outputIndex = index + api.Shift
        previousValue = api.Result[outputIndex - 1]

        if math.isnan(previousValue):
            api.Result[outputIndex] = api.Source[index]
        else:
            api.Result[outputIndex] = previousValue + (api.Source[index] - previousValue) / api.Periods