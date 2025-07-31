import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartSizeEventArgsSample():
    def initialize(self):
        api.Chart.SizeChanged += self.on_chart_size_changed

    def on_chart_size_changed(self, args):
        api.Chart.DrawStaticText("size", "Size Changed", VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)