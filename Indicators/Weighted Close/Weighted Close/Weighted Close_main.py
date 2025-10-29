import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WeightedClose():    
    def calculate(self, index):
        high = api.Bars.HighPrices[index]
        low = api.Bars.LowPrices[index]
        close = api.Bars.ClosePrices[index]
        
        api.Result[index] = (close * 2 + high + low) / 4