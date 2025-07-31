import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartMouseEventArgsSample():
    def initialize(self):
        api.Chart.MouseMove += self.on_chart_mouse_move
        
    def on_chart_mouse_move(self, args):
        text = f"Mouse Location: ({args.MouseX}, {args.MouseY})"
        api.Chart.DrawStaticText("mouse", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)