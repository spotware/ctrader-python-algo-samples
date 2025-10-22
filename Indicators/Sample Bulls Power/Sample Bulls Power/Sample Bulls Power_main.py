import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleBullsPower():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
       
    def calculate(self, index):
        api.Result[index] = api.Bars.HighPrices[index] - self.movingAverage.Result[index]