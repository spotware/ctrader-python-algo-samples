import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartActivationChangedEventArgsSample():
    def initialize(self):
        # Switch to another chart and then switch back to this indicator chart then check the logs
        api.Chart.Activated += self.on_chart_activated
        api.Chart.Deactivated += self.on_chart_deactivated
        
    def on_chart_activated(self, args):
        api.Print(f"Chart {api.Chart.SymbolName} {api.Chart.TimeFrame} with Id {api.Chart.Id} Activated")

    def on_chart_deactivated(self, args):
        api.Print(f"Chart {api.Chart.SymbolName} {api.Chart.TimeFrame} with Id {api.Chart.Id} Deactivated")