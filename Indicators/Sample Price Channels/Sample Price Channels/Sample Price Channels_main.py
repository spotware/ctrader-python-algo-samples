import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import sys

class SamplePriceChannels():        
    def calculate(self, index):
        upper = sys.float_info.min
        lower = sys.float_info.max

        for i in range(index - api.Periods, index):
            upper = max(api.Bars.HighPrices[i], upper)
            lower = min(api.Bars.LowPrices[i], lower)

        api.Upper[index] = upper
        api.Lower[index] = lower
        api.Center[index] = (upper + lower) / 2