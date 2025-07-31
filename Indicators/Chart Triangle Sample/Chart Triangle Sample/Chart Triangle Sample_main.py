import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartTriangleSample():
    def initialize(self):
        x1 = api.Chart.FirstVisibleBarIndex
        x2 = api.Chart.FirstVisibleBarIndex + ((api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex) // 2)
        x3 = api.Chart.LastVisibleBarIndex

        y1 = api.Bars.LowPrices[x1]
        y2 = Functions.Minimum(api.Bars.LowPrices, api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex)
        y3 = api.Bars.HighPrices[x3]

        triangle = api.Chart.DrawTriangle("triangle_sample", x1, y1, x2, y2, x3, y3, Color.FromArgb(100, Color.Red), 2, LineStyle.Dots)

        triangle.IsInteractive = True
        triangle.IsFilled = True