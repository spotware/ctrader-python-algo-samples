import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class RainbowOscillator():
    def initialize(self):
        if api.MAType == MovingAverageType.VIDYA:
            self.indicators = [api.Indicators.MovingAverage(api.Source, i, api.MAType) for i in range(2, api.Levels - 1)]
        else:
            self.indicators = [api.Indicators.MovingAverage(api.Source, api.Levels, api.MAType) for i in range(0, api.Levels - 1)]

    def calculate(self, index):
        aggregatedValue = float("nan")

        for indicator in self.indicators:
            currentValue = api.Source[index] - indicator.Result[index]

            if math.isnan(aggregatedValue):
                aggregatedValue = currentValue
            else:
                aggregatedValue += currentValue

        normalizedValue = aggregatedValue / api.Levels
        api.Result[index] = normalizedValue