import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleEnvelopesCloud():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Bars.ClosePrices, api.Period, MovingAverageType.Simple)
        
    def calculate(self, index):
        maValue = self.movingAverage.Result[index]
        api.UpperBand[index] = maValue * (1 + api.Deviation / 100)
        api.LowerBand[index] = maValue * (1 - api.Deviation / 100)