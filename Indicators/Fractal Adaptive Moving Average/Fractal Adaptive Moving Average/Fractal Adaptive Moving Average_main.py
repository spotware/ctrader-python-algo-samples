import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class FractalAdaptiveMovingAverage():
    def initialize(self):
        self.halfPeriod = api.Periods // 2
        self.dimen = api.CreateDataSeries()
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        previousValue = api.Result[outputIndex - 1]

        if math.isnan(previousValue):
            api.Result[outputIndex] = api.Bars.ClosePrices[index]
            self.dimen[index] = 0
            return

        startBarIndex = index - api.Periods + 1
        n2 = self.n(self.halfPeriod, startBarIndex)
        n1 = self.n(self.halfPeriod, startBarIndex + self.halfPeriod)
        n3 = self.n(api.Periods, startBarIndex)
        
        d = self.dimen[index - 1]
        
        if n1 > 0 and n2 > 0 and n3 > 0:
            d = (math.log10(n1 + n2) - math.log10(n3)) / math.log10(2)
        
        self.dimen[index] = d

        alpha = math.exp(-4.6 * (d - 1))
        alpha = min(alpha, 1)
        alpha = max(alpha, 0.01)

        api.Result[outputIndex] = api.Bars.ClosePrices[index] * alpha + previousValue * (1 - alpha)

    def n(self, length, index):
        if index < 0:
            index = 0
            
        data = [api.Bars[barIndex] for barIndex in range(index, index + length)]
        maxValue = max([b.High for b in data])
        minValue = min([b.Low for b in data])

        return (maxValue - minValue) / length
