import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Aroon():        
    def calculate(self, index):
        if index < api.Periods:
            return

        maxValue = api.Bars.HighPrices[index]
        minValue = api.Bars.LowPrices[index]

        maxPeriod = 0
        minPeriod = 0

        for p in range(api.Periods):
            if api.Bars.HighPrices[index - p] >= maxValue:
                maxValue = api.Bars.HighPrices[index - p]
                maxPeriod = p

            if api.Bars.LowPrices[index - p] <= minValue:
                minValue = api.Bars.LowPrices[index - p]
                minPeriod = p

        api.Up[index] = (api.Periods - maxPeriod - 1) * 100 / (api.Periods - 1)
        api.Down[index] = (api.Periods - minPeriod - 1) * 100 / (api.Periods - 1)