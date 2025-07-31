import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartMouseWheelEventArgsSample():
    def initialize(self):
        api.Chart.MouseWheel += self.on_chart_mouse_wheel
        
    def on_chart_mouse_wheel(self, args):
        text = f"Wheel Delta: {args.Delta}"
        api.Chart.DrawStaticText("wheel", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)