import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AcceleratorOscillator():
    def initialize(self):
        self.awesomeOscillator = api.Indicators.AwesomeOscillator()
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(self.awesomeOscillator.Result, 5)
        
    def calculate(self, index):
        api.Result[index] = self.awesomeOscillator.Result[index] - self.simpleMovingAverage.Result[index]
        api.SetLineAppearance(api.Result.LineOutput, index, 1, api.UpColor if api.Result[index] > api.Result[index - 1] else api.DownColor)
