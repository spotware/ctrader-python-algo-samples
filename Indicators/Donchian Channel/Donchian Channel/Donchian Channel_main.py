import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class DonchianChannel():
    def calculate(self, index):
        if index < api.Periods:
            return

        low = float("nan")
        high = float("nan")

        for i in range(api.Periods + 1):
            currentLow = api.Bars.LowPrices[index - i]
            if currentLow < low or math.isnan(low):
                low = currentLow

            currentHigh = api.Bars.HighPrices[index - i]
            if currentHigh > high or math.isnan(high):
                high = currentHigh

        outputIndex = index + api.Shift

        api.Top[outputIndex] = high
        api.Bottom[outputIndex] = low
        api.Middle[outputIndex] = (high + low) / 2