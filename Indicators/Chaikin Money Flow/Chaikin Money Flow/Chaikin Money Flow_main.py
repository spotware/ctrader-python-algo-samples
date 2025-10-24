import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChaikinMoneyFlow():
    def calculate(self, index):
        if index < api.Periods:
            return

        moneyFlowVolumeSum = 0
        volumeSum = 0

        for i in range(api.Periods):
            close = api.Bars.ClosePrices[index - i]
            low = api.Bars.LowPrices[index - i]
            high = api.Bars.HighPrices[index - i]
            volume = api.Bars.TickVolumes[index - i]

            if high - low != 0:
                moneyFlowMultiplier = (close - low - (high - close)) / (high - low)
                moneyFlowVolume = moneyFlowMultiplier * volume
                moneyFlowVolumeSum += moneyFlowVolume

            volumeSum += volume;

        api.Result[index] = moneyFlowVolumeSum / volumeSum