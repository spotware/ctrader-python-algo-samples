import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LineStyleSample():
    def initialize(self):
        api.Chart.DrawVerticalLine("Dots", api.Chart.LastVisibleBarIndex, Color.Red, 3, LineStyle.Dots);
        api.Chart.DrawVerticalLine("DotsRare", api.Chart.LastVisibleBarIndex - 2, Color.Yellow, 3, LineStyle.DotsRare);
        api.Chart.DrawVerticalLine("DotsVeryRare", api.Chart.LastVisibleBarIndex - 4, Color.Green, 3, LineStyle.DotsVeryRare);
        api.Chart.DrawVerticalLine("Lines", api.Chart.LastVisibleBarIndex - 6, Color.Blue, 3, LineStyle.Lines);
        api.Chart.DrawVerticalLine("LinesDots", api.Chart.LastVisibleBarIndex - 8, Color.Magenta, 3, LineStyle.LinesDots);
        api.Chart.DrawVerticalLine("Solid", api.Chart.LastVisibleBarIndex - 10, Color.Brown, 3, LineStyle.Solid);