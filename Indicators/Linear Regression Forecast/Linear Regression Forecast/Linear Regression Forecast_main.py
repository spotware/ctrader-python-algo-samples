import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LinearRegressionForecast():
    def initialize(self):
        self.slope = api.Indicators.LinearRegressionSlope(api.Source, api.Periods)
        self.intercept = api.Indicators.LinearRegressionIntercept(api.Source, api.Periods)
        
    def calculate(self, index):
        api.Result[index + api.Shift] = api.Periods * self.slope.Result[index] + self.intercept.Result[index]