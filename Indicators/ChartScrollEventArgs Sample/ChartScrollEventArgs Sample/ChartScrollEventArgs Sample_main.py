import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartScrollEventArgsSample():
    def initialize(self):
        api.Chart.ScrollChanged += self.on_chart_scroll_changed

    def on_chart_scroll_changed(self, args):
        api.Print(f"Scrolled, Bars Delta : {args.BarsDelta} | Top Y Delta: {args.TopYDelta} | Bottom Y Delta: {args.BottomYDelta}")