import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartObjectHoverChangedEventArgsSample():
    def initialize(self):
        api.Chart.ObjectHoverChanged += self.on_chart_object_hover_changed
        
    def on_chart_object_hover_changed(self, args):
        text = f"Is Object Hovered: {args.IsObjectHovered}"
        api.Chart.DrawStaticText("hover", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)