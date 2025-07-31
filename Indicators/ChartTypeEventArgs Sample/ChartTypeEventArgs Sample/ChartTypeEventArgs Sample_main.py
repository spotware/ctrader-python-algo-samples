import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartTypeEventArgsSample():
    def initialize(self):
        api.Chart.ChartTypeChanged += self.on_chart_type_changed

    def on_chart_type_changed(self, args):
        text = f"Chart Type Changed To: {args.Chart.ChartType}"
        api.Chart.DrawStaticText("type", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)