import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class StochasticOscillator():
    def initialize(self):
        self.fastK = api.CreateDataSeries()
        self.slowK = api.Indicators.MovingAverage(self.fastK, api.KSlowing, api.MAType)

        self.averageOnSlowK = api.Indicators.MovingAverage(self.slowK.Result, api.DPeriods, api.MAType)
        
    def calculate(self, index):
        self.fastK[index] = self.get_fast_k_value(index)

        api.PercentK[index] = self.slowK.Result[index]
        api.PercentD[index] = self.averageOnSlowK.Result[index]

    def get_fast_k_value(self, index):
        lowestLow = self.get_min_from_period(api.Bars.LowPrices if api.CalculationType == StochasticCalculationType.LowHigh else api.Bars.ClosePrices, index, api.KPeriods)

        hightestHigh = self.get_max_from_period(api.Bars.HighPrices if api.CalculationType == StochasticCalculationType.LowHigh else api.Bars.ClosePrices, index, api.KPeriods)

        currentClose = api.Bars.ClosePrices[index]

        return (currentClose - lowestLow) / (hightestHigh - lowestLow) * 100

    def get_min_from_period(self, dataSeries, endIndex, periods):
        minValue = dataSeries[endIndex]

        for i in reversed(range(endIndex - periods + 1, endIndex)):
            if (dataSeries[i] < minValue):
                minValue = dataSeries[i]

        return minValue;

    def get_max_from_period(self, dataSeries, endIndex, periods):
        maxValue = dataSeries[endIndex]

        for i in reversed(range(endIndex - periods + 1, endIndex)):
            if (dataSeries[i] > maxValue):
                maxValue = dataSeries[i]

        return maxValue;