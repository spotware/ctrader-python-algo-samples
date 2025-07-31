import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartObjectsSelectionChangedEventArgsSample():
    def initialize(self):
        api.Chart.ObjectsSelectionChanged += self.on_chart_objects_selection_changed

    def on_chart_objects_selection_changed(self, args):
        api.Print(f"Added objects #: {args.ObjectsAddedToSelection.Count} | Removed Objects #: {args.ObjectsRemovedFromSelection.Count}")