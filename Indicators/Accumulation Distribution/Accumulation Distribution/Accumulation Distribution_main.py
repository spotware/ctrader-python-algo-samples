import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class AccumulationDistribution():        
    def calculate(self, index):
        previousValue = 0 if math.isnan(api.Result[index - 1]) else api.Result[index - 1]

        close = api.Bars.ClosePrices[index]
        low = api.Bars.LowPrices[index]
        high = api.Bars.HighPrices[index]
        volume = api.Bars.TickVolumes[index]

        if high - low == 0:
            api.Result[index] = previousValue
            return

        closeLocationValue = (close - low - (high - close)) / (high - low)
        moneyFlowVolume = closeLocationValue * volume

        api.Result[index] = previousValue + moneyFlowVolume