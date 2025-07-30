import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartIconSample():
    def initialize(self):
        for i in range(api.Chart.FirstVisibleBarIndex, api.Chart.LastVisibleBarIndex):
            iconName = f"Icon_{i}"
            if api.Bars.ClosePrices[i] > api.Bars.OpenPrices[i]:
                api.Chart.DrawIcon(iconName, ChartIconType.UpArrow, i, api.Bars.LowPrices[i], Color.Green)
            else:
                api.Chart.DrawIcon(iconName, ChartIconType.DownArrow, i, api.Bars.HighPrices[i], Color.Red)
