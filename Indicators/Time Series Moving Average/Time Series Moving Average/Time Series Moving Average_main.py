import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TimeSeriesMovingAverage():
    def initialize(self):
        self.linearRegressionForecast = api.Indicators.LinearRegressionForecast(api.Source, api.Periods)

    def calculate(self, index):
        api.Result[index + api.Shift] = self.linearRegressionForecast.Result[index]
