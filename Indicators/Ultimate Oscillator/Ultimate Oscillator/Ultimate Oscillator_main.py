import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class UltimateOscillator():
    def calculate(self, index):
        average1 = self.calculate_average_buying_pressure(index, api.Cycle1)
        average2 = self.calculate_average_buying_pressure(index, api.Cycle2)
        average3 = self.calculate_average_buying_pressure(index, api.Cycle3)

        api.Result[index] = (4 * average1 + 2 * average2 + average3) / (4 + 2 + 1) * 100

    def calculate_average_buying_pressure(self, index, periods):
        totalBuyingPressure = 0
        totalTrueRange = 0

        for i in reversed(range(periods)):
            buyingPressure = self.calculate_buying_pressure(index - i)
            trueRange = self.calculate_true_range(index - i)

            totalBuyingPressure += buyingPressure
            totalTrueRange += trueRange

        return totalBuyingPressure / totalTrueRange

    def calculate_true_range(self, period):
        return max(api.Bars.HighPrices[period], api.Bars.ClosePrices[period - 1]) - min(api.Bars.LowPrices[period], api.Bars.ClosePrices[period - 1])

    def calculate_buying_pressure(self, period):
        return api.Bars.ClosePrices[period] - min(api.Bars.LowPrices[period], api.Bars.ClosePrices[period - 1])