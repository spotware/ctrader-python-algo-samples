import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MacdOscillatorMovingAverage():
    def initialize(self):
        self.macd = api.Indicators.MacdHistogram(api.Source, api.LongCycle, api.ShortCycle, api.SignalPeriods)
        self.osma = api.Indicators.OscillatorMovingAverage(self.macd.Histogram, api.SignalPeriods, api.MAType)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.Histogram[outputIndex] = self.osma.Histogram[index]