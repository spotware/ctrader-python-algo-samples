import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FibonacciLevelSample():
    def initialize(self):
        period = api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex

        maxValue = Functions.Maximum(api.Bars.HighPrices, period)
        minValue = Functions.Minimum(api.Bars.LowPrices, period)

        fibonacciRetracement = api.Chart.DrawFibonacciRetracement(
            "FibonacciRetracement",
            api.Chart.FirstVisibleBarIndex,
            maxValue,
            api.Chart.LastVisibleBarIndex,
            minValue,
            Color.Red)

        for level in fibonacciRetracement.FibonacciLevels:
            api.Print(level.PercentLevel)
            if level.PercentLevel > 62:
                level.IsVisible = False