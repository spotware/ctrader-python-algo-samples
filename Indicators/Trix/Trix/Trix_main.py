import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Trix():
    def initialize(self):
        self.singleSmoothed = api.Indicators.ExponentialMovingAverage(api.Source, api.Periods)
        self.doubleSmoothed = api.Indicators.ExponentialMovingAverage(self.singleSmoothed.Result, api.Periods)
        self.tripleSmoothed = api.Indicators.ExponentialMovingAverage(self.doubleSmoothed.Result, api.Periods)
        
    def calculate(self, index):
        previous = self.tripleSmoothed.Result[index - 1]
        current = self.tripleSmoothed.Result[index]

        api.Result[index] = (current - previous) / previous * 100