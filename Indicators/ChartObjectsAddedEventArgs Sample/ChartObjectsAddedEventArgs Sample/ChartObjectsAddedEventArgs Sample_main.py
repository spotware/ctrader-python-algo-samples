import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartObjectsAddedEventArgsSample():
    def initialize(self):
        api.Chart.ObjectsAdded += self.on_chart_objects_added
        
    def on_chart_objects_added(self, args):
        api.Print(f"{args.ChartObjects.Count} objects added to chart")