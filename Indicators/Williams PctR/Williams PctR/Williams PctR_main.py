import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WilliamsPctR():
    def calculate(self, index):
        highest = api.Bars.HighPrices[index]
        lowest = api.Bars.LowPrices[index]

        for i in range(index - api.Periods + 1, index + 1):
            highest = max(highest, api.Bars.HighPrices[i])
            lowest = min(lowest, api.Bars.LowPrices[i])

        api.Result[index] = (highest - api.Bars.ClosePrices[index]) / (highest - lowest) * -100