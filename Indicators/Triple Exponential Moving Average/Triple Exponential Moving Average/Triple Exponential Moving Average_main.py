import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TripleExponentialMovingAverage():
    def initialize(self):
        self.ema1 = api.Indicators.MovingAverage(api.Source, api.Periods, MovingAverageType.Exponential)
        self.ema2 = api.Indicators.MovingAverage(self.ema1.Result, api.Periods, MovingAverageType.Exponential)
        self.ema3 = api.Indicators.MovingAverage(self.ema2.Result, api.Periods, MovingAverageType.Exponential)
        
    def calculate(self, index):
        api.Result[index + api.Shift] = 3 * self.ema1.Result[index] - 3 * self.ema2.Result[index] + self.ema3.Result[index]