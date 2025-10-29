import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PriceOscillator():
    def initialize(self):
        self.longMa = api.Indicators.MovingAverage(api.Source, api.LongCycle, api.MAType)
        self.shortMa = api.Indicators.MovingAverage(api.Source, api.ShortCycle, api.MAType)
        
    def calculate(self, index):
        shortValue = self.shortMa.Result[index]
        longValue = self.longMa.Result[index]

        api.Result[index] = (shortValue - longValue) / longValue * 100