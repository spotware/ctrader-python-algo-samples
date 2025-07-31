import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartColorEventArgsSample():
    def initialize(self):
        api.Chart.ColorsChanged += self.on_chart_colors_changed

    def on_chart_colors_changed(self, args):
        api.Print(f"Chart {args.Chart.SymbolName} {args.Chart.TimeFrame} Color changed")