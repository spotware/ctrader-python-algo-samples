import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AverageTrueRange():
    def initialize(self):
        trueRange = api.Indicators.TrueRange()
        self.movingAverage = api.Indicators.MovingAverage(trueRange.Result, api.Periods, api.MAType)
        
    def calculate(self, index):
        api.Result[index] = self.movingAverage.Result[index]