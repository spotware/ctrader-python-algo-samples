import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IndicatorAreaAddedEventArgsSample():
    def initialize(self):
        self.show_indicator_areas_count()
        api.Chart.IndicatorAreaAdded += self.on_chart_indicator_area_added

    def on_chart_indicator_area_added(self, args):
        api.Print("A new indicator area has been added")
        self.show_indicator_areas_count()

    def show_indicator_areas_count(self):
        text = f"Indicator Areas #: {api.Chart.IndicatorAreas.Count}"
        api.Chart.DrawStaticText("text", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)