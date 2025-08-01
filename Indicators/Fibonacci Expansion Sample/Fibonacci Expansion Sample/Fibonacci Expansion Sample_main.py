import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FibonacciExpansionSample():
    def initialize(self):
        period = api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex

        fibonacciExpansion = api.Chart.DrawFibonacciExpansion(
            "fibonacciExpansion",
            api.Chart.FirstVisibleBarIndex,
            api.Bars.LowPrices[api.Chart.FirstVisibleBarIndex],
            api.Chart.FirstVisibleBarIndex,
            Functions.Minimum(api.Bars.LowPrices, period),
            api.Chart.LastVisibleBarIndex,
            Functions.Maximum(api.Bars.HighPrices, period),
            Color.Red)

        fibonacciExpansion.IsInteractive = True