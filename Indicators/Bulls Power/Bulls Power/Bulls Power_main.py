import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BullsPower():
    def initialize(self):
        self.ma = api.Indicators.MovingAverage(api.Bars.ClosePrices, api.Periods, api.MAType)
      
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.Result[outputIndex] = api.Bars.HighPrices[index] - self.ma.Result[index]