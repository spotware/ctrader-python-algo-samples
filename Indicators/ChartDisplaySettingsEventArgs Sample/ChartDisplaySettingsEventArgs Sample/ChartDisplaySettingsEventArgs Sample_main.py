import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartDisplaySettingsEventArgsSample():
    def initialize(self):
        api.Chart.DisplaySettingsChanged += self.on_chart_display_settings_changed
        
    def on_chart_display_settings_changed(self, args):
        api.Print(f"Chart {args.Chart.SymbolName} {args.Chart.TimeFrame} Display settings changed")