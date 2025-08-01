import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FibonacciFanSample():
    def initialize(self):
        api.Chart.DrawFibonacciFan(
            "Fan",
            api.Chart.FirstVisibleBarIndex,
            api.Bars.ClosePrices[api.Chart.FirstVisibleBarIndex],
            api.Chart.LastVisibleBarIndex,
            api.Bars.ClosePrices[api.Chart.LastVisibleBarIndex],
            Color.Red)