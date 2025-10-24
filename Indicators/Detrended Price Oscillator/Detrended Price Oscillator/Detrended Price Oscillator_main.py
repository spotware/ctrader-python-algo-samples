import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class DetrendedPriceOscillator():
    def initialize(self):
        self.ma = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)

    def calculate(self, index):
        api.Result[index] = api.Source[index] - self.ma.Result[index - api.Periods // 2 - 1]