import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class KaufmanAdaptiveMovingAverage():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Bars.ClosePrices
     
    def calculate(self, index):
        outputIndex = index + api.Shift
        previousValue = api.Result[outputIndex - 1]

        if index < api.Periods:
            return

        if math.isnan(previousValue):
            api.Result[outputIndex] = api.Source[index]
            return

        direction = abs(api.Source[index] - api.Source[index - api.Periods])

        v0 = [api.Source[i] for i in range(index - api.Periods, index + api.Periods)]
        v1 = [api.Source[i] for i in range(index - api.Periods - 1, index + api.Periods - 1)]

        volatility = sum([abs(v0[i] - v1[i]) for i in range(len(v0))])

        er = direction / volatility
        fastSc = 2.0 / (api.FastPeriods + 1)
        slowSc = 2.0 / (api.SlowPeriods + 1)
        sc = pow(er * (fastSc - slowSc) + slowSc, 2)

        api.Result[outputIndex] = previousValue + sc * (api.Source[index] - previousValue)