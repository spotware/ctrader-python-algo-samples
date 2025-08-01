import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IndicatorAreaRemovedEventArgsSample():
    def initialize(self):
        self.show_indicator_areas_count()
        api.Chart.IndicatorAreaRemoved += self.on_chart_indicator_area_removed

    def on_chart_indicator_area_removed(self, args):
        api.Print("An indicator area has been removed")
        self.show_indicator_areas_count()

    def show_indicator_areas_count(self):
        text = f"Indicator Areas #: {api.Chart.IndicatorAreas.Count}"
        api.Chart.DrawStaticText("text", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)