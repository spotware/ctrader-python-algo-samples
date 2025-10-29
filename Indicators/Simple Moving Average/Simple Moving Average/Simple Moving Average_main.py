import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SimpleMovingAverage():
    def calculate(self, index):
        outputIndex = index + api.Shift

        sumValue = 0

        startBarIndex = index - api.Periods + 1

        for i in range(startBarIndex, index + 1):
            sumValue += api.Source[i]

        api.Result[outputIndex] = sumValue / api.Periods