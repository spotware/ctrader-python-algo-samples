import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AwesomeOscillator():
    def initialize(self):
        self.sma5 = api.Indicators.SimpleMovingAverage(api.Bars.MedianPrices, 5)
        self.sma34 = api.Indicators.SimpleMovingAverage(api.Bars.MedianPrices, 34)
        
    def calculate(self, index):
        api.Result[index] = self.sma5.Result[index] - self.sma34.Result[index]
        api.SetLineAppearance(api.Result.LineOutput, index, 1, api.UpColor if api.Result[index] > api.Result[index - 1] else api.DownColor)
