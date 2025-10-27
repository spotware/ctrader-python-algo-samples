import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MacdCrossover():
    def initialize(self):
        self.emaLong = api.Indicators.ExponentialMovingAverage(api.Source, api.LongCycle)
        self.emaShort = api.Indicators.ExponentialMovingAverage(api.Source, api.ShortCycle)
        self.emaSignal = api.Indicators.ExponentialMovingAverage(api.MACD, api.SignalPeriods)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.MACD[outputIndex] = self.emaShort.Result[index] - self.emaLong.Result[index]
        api.Signal[outputIndex] = self.emaSignal.Result[index]
        api.Histogram[outputIndex] = api.MACD[outputIndex] - api.Signal[outputIndex]