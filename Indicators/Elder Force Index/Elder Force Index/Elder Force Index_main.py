import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ElderForceIndex():
    def initialize(self):
        self.fi = api.CreateDataSeries()
        self.ma = api.Indicators.MovingAverage(self.fi, api.Periods, api.MAType)
        
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index < 1:
            api.Result[outputIndex] = float("nan")
            return

        self.fi[index] = (api.Bars.ClosePrices[index] - api.Bars.ClosePrices[index - 1]) * api.Bars.TickVolumes[index]
        
        api.Result[outputIndex] = self.ma.Result[index]