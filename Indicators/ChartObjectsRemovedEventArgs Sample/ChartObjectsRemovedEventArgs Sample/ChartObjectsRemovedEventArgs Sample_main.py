import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartObjectsRemovedEventArgsSample():
    def initialize(self):
        api.Chart.ObjectsRemoved += self.on_chart_objects_removed

    def on_chart_objects_removed(self, args):
        api.Print(f"{args.ChartObjects.Count} objects removed from chart")