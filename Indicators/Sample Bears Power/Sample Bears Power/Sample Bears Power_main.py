import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleBearsPower():
    def initialize(self):
        self.movingAverage = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType);

    def calculate(self, index):
        api.Result[index] = api.Bars.LowPrices[index] - self.movingAverage.Result[index];
