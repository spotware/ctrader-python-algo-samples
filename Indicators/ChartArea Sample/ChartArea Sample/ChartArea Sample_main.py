import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartAreaSample():
    def initialize(self):
        self.draw_static_text(api.Chart, "a", "Chart");
        self.draw_static_text(api.IndicatorArea, "b", "Indicator");
        
    def draw_static_text(self, area, name, text):
        area.DrawStaticText(name, text, VerticalAlignment.Center, HorizontalAlignment.Center, Color.Red)