import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartRectangleSample():
    def initialize(self):
        period = api.Chart.LastVisibleBarIndex - api.Chart.FirstVisibleBarIndex

        rectangle = api.Chart.DrawRectangle("rectangle_sample", api.Chart.FirstVisibleBarIndex, Functions.Minimum(api.Bars.LowPrices, period), api.Chart.LastVisibleBarIndex, Functions.Maximum(api.Bars.HighPrices, period), Color.FromArgb(100, Color.Red))

        rectangle.IsFilled = True
        rectangle.IsInteractive = True