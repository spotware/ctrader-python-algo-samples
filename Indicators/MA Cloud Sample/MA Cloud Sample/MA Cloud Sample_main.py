import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MACloudSample():
    def initialize(self):
        self.fastMA = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 7)
        self.slowMA = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 13)
    
    def calculate(self, index):
        api.Fast[index] = self.fastMA.Result[index]
        api.Slow[index] = self.slowMA.Result[index]