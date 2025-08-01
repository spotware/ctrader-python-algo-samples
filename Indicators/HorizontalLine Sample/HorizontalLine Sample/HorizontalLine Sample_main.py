import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class HorizontalLineSample():
    def initialize(self):
        api.Chart.DrawHorizontalLine("horizontalLine", api.Bars.ClosePrices.LastValue, Color.Red)