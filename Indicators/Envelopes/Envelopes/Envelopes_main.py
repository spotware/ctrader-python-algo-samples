import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Envelopes():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Bars.ClosePrices
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        maValue = self.movingAverage.Result[index]
        
        api.Main[outputIndex] = maValue
        api.Upper[outputIndex] = maValue * (1 + api.Deviation / 100)
        api.Lower[outputIndex] = maValue * (1 - api.Deviation / 100)