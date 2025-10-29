import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TrueRange():  
    def calculate(self, index):
        high = api.Bars.HighPrices[index]
        low = api.Bars.LowPrices[index]
        previousClose = api.Bars.ClosePrices[index - 1]

        api.Result[index] = max(high, previousClose) - min(low, previousClose)