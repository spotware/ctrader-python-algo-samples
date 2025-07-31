import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartTrendLineSample():
    def initialize(self):
        trendLine = api.Chart.DrawTrendLine("trendLine", api.Chart.FirstVisibleBarIndex, api.Bars.LowPrices[api.Chart.FirstVisibleBarIndex], api.Chart.LastVisibleBarIndex, api.Bars.HighPrices[api.Chart.LastVisibleBarIndex], Color.Red, 2, LineStyle.Dots)
        trendLine.IsInteractive = True