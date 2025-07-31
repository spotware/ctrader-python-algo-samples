import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartKeyboardEventArgsSample():
    def initialize(self):
        api.Chart.KeyDown += self.on_chart_key_down
        
    def on_chart_key_down(self, args):
        api.Print(f"Key: {args.Key} | Modifier Key: {args.Modifiers}")