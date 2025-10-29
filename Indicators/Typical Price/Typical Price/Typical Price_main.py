import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TypicalPrice(): 
    def calculate(self, index):
        api.Result[index] = (api.Bars.HighPrices[index] + api.Bars.LowPrices[index] + api.Bars.ClosePrices[index]) / 3