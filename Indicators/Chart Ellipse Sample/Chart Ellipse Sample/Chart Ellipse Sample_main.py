import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartEllipseSample():
    def initialize(self):
        self.draw()
        
    def calculate(self, index):
        self.draw()

    def draw(self):
        y1 = api.Bars.HighPrices[api.Chart.FirstVisibleBarIndex] if api.Bars.HighPrices[api.Chart.FirstVisibleBarIndex] > api.Bars.HighPrices[api.Chart.LastVisibleBarIndex] else api.Bars.HighPrices[api.Chart.LastVisibleBarIndex]
        y2 = api.Bars.LowPrices[api.Chart.FirstVisibleBarIndex] if api.Bars.LowPrices[api.Chart.FirstVisibleBarIndex] < api.Bars.LowPrices[api.Chart.LastVisibleBarIndex] else api.Bars.LowPrices[api.Chart.LastVisibleBarIndex]

        ellipse = api.Chart.DrawEllipse("ellipse", api.Chart.FirstVisibleBarIndex, y1, api.Chart.LastVisibleBarIndex, y2, Color.FromArgb(50, Color.Red.R, Color.Red.G, Color.Red.B))
        ellipse.IsFilled = True