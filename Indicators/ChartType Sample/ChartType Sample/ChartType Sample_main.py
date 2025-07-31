import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartTypeSample():
    def initialize(self):
        self.show_chart_type()
        api.Chart.ChartTypeChanged += lambda _: self.show_chart_type()

    def show_chart_type(self):
        api.Chart.DrawStaticText("type", f"Type: {api.Chart.ChartType}", VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)