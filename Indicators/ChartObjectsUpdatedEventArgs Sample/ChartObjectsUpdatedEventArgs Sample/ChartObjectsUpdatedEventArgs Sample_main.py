import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartObjectsUpdatedEventArgsSample():
    def initialize(self):
        api.Chart.ObjectsUpdated += self.on_chart_objects_updated

    def on_chart_objects_updated(self, args):
        api.Print(f"Updated objects #: {args.ChartObjects.Count}")