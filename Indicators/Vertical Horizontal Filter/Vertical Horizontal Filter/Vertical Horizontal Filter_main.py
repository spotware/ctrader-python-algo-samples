import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class VerticalHorizontalFilter():
    def calculate(self, index):
        maxValue = api.Source[index]
        minValue = api.Source[index]
        sumValue = 0

        for i in range(index - api.Periods + 1, index + 1):
            maxValue = max(maxValue, api.Source[i])
            minValue = min(minValue, api.Source[i])
            sumValue += abs(api.Source[i] - api.Source[i - 1])

        api.Result[index] = abs((maxValue - minValue) / sumValue)