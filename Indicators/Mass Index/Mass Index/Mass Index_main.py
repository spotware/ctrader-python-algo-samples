import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MassIndex():
    def initialize(self):
        self.highMinusLow = api.Indicators.HighMinusLow()
        self.movingAverage1 = api.Indicators.ExponentialMovingAverage(self.highMinusLow.Result, 9)
        self.movingAverage2 = api.Indicators.ExponentialMovingAverage(self.movingAverage1.Result, 9)
        
    def calculate(self, index):
        firstAverageSeries = self.get_period(self.movingAverage1.Result, index + 1, api.Periods + 1)[:api.Periods]
        secondAverageSeries = self.get_period(self.movingAverage2.Result, index + 1, api.Periods + 1)[:api.Periods]

        api.Result[index] = sum([firstAverageSeries[i] / secondAverageSeries[i] for i in range(len(firstAverageSeries))])

    def get_period(self, values, index, periods):
        return [values[i] for i in range(index + 1 - periods, index + 1 + periods)]
