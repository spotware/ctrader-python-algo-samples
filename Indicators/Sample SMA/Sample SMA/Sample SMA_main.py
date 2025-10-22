import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleSMA():
    def calculate(self, index):
        sumValue = 0

        for i in range(index - api.Periods + 1, index + 1):
            sumValue += api.Source[i]

        api.Result[index] = sumValue / api.Periods