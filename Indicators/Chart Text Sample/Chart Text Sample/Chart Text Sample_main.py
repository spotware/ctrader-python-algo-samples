import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartTextSample():
    def initialize(self):
        for iBarIndex in range(api.Chart.FirstVisibleBarIndex, api.Chart.LastVisibleBarIndex + 1):
            if api.Bars.ClosePrices[iBarIndex] > api.Bars.OpenPrices[iBarIndex]:
                text = "U"
                y = api.Bars.LowPrices[iBarIndex]
                color = Color.Green
            else:
                text = "D"
                y = api.Bars.HighPrices[iBarIndex]
                color = Color.Red

            api.Chart.DrawText(f"Text_{iBarIndex}", text, iBarIndex, y, color)