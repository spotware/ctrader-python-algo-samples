import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartIdSample():
    def initialize(self):
        api.Print(f"Current chart Id is: {api.Chart.Id}")

        api.Chart.Activated += self.on_chart_activated
        api.Chart.Deactivated += self.on_chart_deactivated
        
    def on_chart_activated(self, args):
        api.Print(f"Chart with Id {api.Chart.Id} Activated")

    def on_chart_deactivated(self, args):
        api.Print(f"Chart with Id {api.Chart.Id} Deactivated")