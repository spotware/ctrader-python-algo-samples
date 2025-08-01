import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IIndicatorsAccessorSample():
    def initialize(self):
        self.sma = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 20)
    
    def calculate(self, index):
        api.Result[index] = self.sma.Result[index]