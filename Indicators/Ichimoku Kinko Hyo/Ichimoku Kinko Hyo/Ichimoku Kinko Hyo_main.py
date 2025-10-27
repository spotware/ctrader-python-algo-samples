import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IchimokuKinkoHyo(): 
    def calculate(self, index):
        if index < api.TenkanSenPeriods or index < api.SenkouSpanBPeriods:
            return

        maxFast = api.Bars.HighPrices[index]
        minFast = api.Bars.LowPrices[index]
        maxMedium = api.Bars.HighPrices[index]
        minMedium = api.Bars.LowPrices[index]
        maxSlow = api.Bars.HighPrices[index]
        minSlow = api.Bars.LowPrices[index]

        for i in range(api.TenkanSenPeriods):
            if maxFast < api.Bars.HighPrices[index - i]:
                maxFast = api.Bars.HighPrices[index - i]

            if minFast > api.Bars.LowPrices[index - i]:
                minFast = api.Bars.LowPrices[index - i]

        for i in range(api.KijunSenPeriods):
            if maxMedium < api.Bars.HighPrices[index - i]:
                maxMedium = api.Bars.HighPrices[index - i]

            if minMedium > api.Bars.LowPrices[index - i]:
                minMedium = api.Bars.LowPrices[index - i]

        for i in range(api.SenkouSpanBPeriods):
            if maxSlow < api.Bars.HighPrices[index - i]:
                maxSlow = api.Bars.HighPrices[index - i]

            if minSlow > api.Bars.LowPrices[index - i]:
                minSlow = api.Bars.LowPrices[index - i]

        api.TenkanSen[index + api.Shift] = (maxFast + minFast) / 2
        api.KijunSen[index + api.Shift] = (maxMedium + minMedium) / 2

        api.ChikouSpan[index - api.KijunSenPeriods + api.Shift] = api.Bars.ClosePrices[index]

        api.SenkouSpanA[index + api.KijunSenPeriods + api.Shift] = (api.TenkanSen[index + api.Shift] + api.KijunSen[index + api.Shift]) / 2
        api.SenkouSpanB[index + api.KijunSenPeriods + api.Shift] = (maxSlow + minSlow) / 2