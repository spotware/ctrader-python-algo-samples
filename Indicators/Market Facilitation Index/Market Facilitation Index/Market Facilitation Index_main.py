import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MarketFacilitationIndex():
    def calculate(self, index):
        api.Result[index + api.Shift] =  0 if api.Bars.TickVolumes[index] == 0 else (api.Bars.HighPrices[index] - api.Bars.LowPrices[index]) / api.Bars.TickVolumes[index]