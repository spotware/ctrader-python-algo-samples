import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FunctionsSample():
    def initialize(self):
        self.fastSma = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 9)
        self.slowSma = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 20)

    def calculate(self, index):
        if Functions.HasCrossedAbove(self.fastSma.Result, self.slowSma.Result, 1):
            api.Print("Fast MA crossed above slow MA")

        if Functions.HasCrossedBelow(self.fastSma.Result, self.slowSma.Result, 1):
            api.Print("Fast MA crossed below slow MA")

        if Functions.Maximum(self.fastSma.Result, 10) > Functions.Maximum(self.slowSma.Result, 10):
            api.Print("Fast MA last 10 values maximum is larger than slow MA last 10 values")

        if Functions.Minimum(self.fastSma.Result, 10) < Functions.Minimum(self.slowSma.Result, 10):
            api.Print("Fast MA last 10 values minimum is smaller than slow MA last 10 values")

        # IsFalling and IsRising compares last two values of the data series
        if Functions.IsFalling(self.fastSma.Result) and Functions.IsRising(self.slowSma.Result):
            api.Print("Fast MA is falling and slow MA is raising")

        if Functions.Sum(self.fastSma.Result, 10) > Functions.Sum(self.slowSma.Result, 10):
            api.Print("Fast MA last 10 values sum is larger than slow MA last 109 values sum")