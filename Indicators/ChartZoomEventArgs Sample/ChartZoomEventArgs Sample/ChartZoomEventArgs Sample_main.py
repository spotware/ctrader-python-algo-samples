import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartZoomEventArgsSample():
    def initialize(self):
        api.Chart.ZoomChanged += self.on_chart_zoom_changed

    def on_chart_zoom_changed(self, args):
        text = f"Chart Zoom Level Changed To: {args.Chart.ZoomLevel}"
        api.Chart.DrawStaticText("type", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)