import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class DoubleExponentialMovingAverage():
    def initialize(self):
        self.movingAverageOverSource = api.Indicators.MovingAverage(api.Source, api.Periods, MovingAverageType.Exponential)
        self.movingAverageOverMovingAverage = api.Indicators.MovingAverage(self.movingAverageOverSource.Result, api.Periods, MovingAverageType.Exponential)
        
    def calculate(self, index):
        api.Result[index + api.Shift] = 2 * self.movingAverageOverSource.Result[index] - self.movingAverageOverMovingAverage.Result[index]