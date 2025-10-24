import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CommodityChannelIndex():
    def initialize(self):
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.Source, api.Periods)

    def calculate(self, index):
        if index < 2 * api.Periods:
            return

        meanDeviation = 0

        simpleMaValue = self.simpleMovingAverage.Result[index]
        
        for count in range(index - api.Periods, index):
            meanDeviation += abs(api.Source[count] - simpleMaValue)

        meanDeviation /= api.Periods
        api.Result[index + api.Shift] = (api.Source[index] - simpleMaValue) / (meanDeviation * 0.015)