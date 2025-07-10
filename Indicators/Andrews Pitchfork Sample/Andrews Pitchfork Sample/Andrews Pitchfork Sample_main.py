import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AndrewsPitchforkSample():
    def initialize(self):
        barIndex1 = api.Chart.FirstVisibleBarIndex
        barIndex2 = api.Chart.FirstVisibleBarIndex + ((api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex) // 5)
        barIndex3 = api.Chart.FirstVisibleBarIndex + ((api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex) // 2)

        y1 = api.Bars.ClosePrices[barIndex1]
        y2 = api.Bars.ClosePrices[barIndex2]
        y3 = api.Bars.ClosePrices[barIndex3]
       
        andrewsPitchfork = api.Chart.DrawAndrewsPitchfork("AndrewsPitchfork", barIndex1, y1, barIndex2, y2, barIndex3, y3, Color.Red)
        andrewsPitchfork.IsInteractive = True