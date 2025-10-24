import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BollingerBands():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
        self.standardDeviation = api.Indicators.StandardDeviation(api.Source, api.Periods, api.MAType)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        deviationShift = self.standardDeviation.Result[index] * api.StandardDeviations

        api.Main[outputIndex] = self.movingAverage.Result[index]
        api.Bottom[outputIndex] = self.movingAverage.Result[index] - deviationShift
        api.Top[outputIndex] = self.movingAverage.Result[index] + deviationShift