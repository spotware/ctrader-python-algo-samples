import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MacdHistogram():
    def initialize(self):
        self.emaLong = api.Indicators.ExponentialMovingAverage(api.Source, api.LongCycle)
        self.emaShort = api.Indicators.ExponentialMovingAverage(api.Source, api.ShortCycle)
        self.emaSignal = api.Indicators.ExponentialMovingAverage(api.Histogram, api.SignalPeriods)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.Histogram[outputIndex] = self.emaShort.Result[index] - self.emaLong.Result[index]
        api.Signal[outputIndex] = self.emaSignal.Result[index]