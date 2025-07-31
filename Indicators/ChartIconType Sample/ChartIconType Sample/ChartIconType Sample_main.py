import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartIconTypeSample():
    def initialize(self):
        api.Chart.DrawIcon("Icon", api.IconType, api.Chart.LastVisibleBarIndex, api.Chart.Bars.LastBar.Low, Color.Red);