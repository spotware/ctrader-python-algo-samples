import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LevelsSample():
    def initialize(self):
        self.rsi = api.Indicators.RelativeStrengthIndex(api.Bars.ClosePrices, api.Periods)

    def calculate(self, index):
        api.Result[index] = self.rsi.Result[index]