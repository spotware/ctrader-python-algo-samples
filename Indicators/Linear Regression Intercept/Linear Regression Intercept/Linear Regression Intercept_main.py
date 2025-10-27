import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class LinearRegressionIntercept():
    def initialize(self):
        self.slope = api.Indicators.LinearRegressionSlope(api.Source, api.Periods)
        self.sma = api.Indicators.SimpleMovingAverage(api.Source, api.Periods)
        
    def calculate(self, index):
        api.Result[index + api.Shift] = self.sma.Result[index] - self.slope.Result[index] * math.floor(api.Periods * 1.0 / 2)
