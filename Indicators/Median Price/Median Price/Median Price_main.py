import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MedianPrice():    
    def calculate(self, index):
        api.Result[index + api.Shift] = (api.Bars.HighPrices[index] + api.Bars.LowPrices[index]) / 2