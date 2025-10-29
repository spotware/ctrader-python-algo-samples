import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class OscillatorMovingAverage():
    def initialize(self):
        self.ma = api.Indicators.MovingAverage(api.Source, api.Periods, api.MAType)
        
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.Histogram[outputIndex] = api.Source[index] - self.ma.Result[index]