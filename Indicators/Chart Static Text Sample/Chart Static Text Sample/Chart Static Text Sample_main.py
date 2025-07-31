import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartStaticTextSample():
    def initialize(self):
        text = f"""
Symbol: {api.SymbolName}
TimeFrame: {api.TimeFrame}
Chart Type: {api.Chart.ChartType}"""

        api.Chart.DrawStaticText("Static_Sample", text, VerticalAlignment.Bottom, HorizontalAlignment.Left, Color.Red)