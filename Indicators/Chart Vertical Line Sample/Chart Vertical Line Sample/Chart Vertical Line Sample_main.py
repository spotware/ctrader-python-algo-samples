import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartVerticalLineSample():
    def initialize(self):
        verticalLine = api.Chart.DrawVerticalLine("vertical_line", api.Chart.LastVisibleBarIndex, Color.Red, 2, LineStyle.DotsRare)
        verticalLine.IsInteractive = True