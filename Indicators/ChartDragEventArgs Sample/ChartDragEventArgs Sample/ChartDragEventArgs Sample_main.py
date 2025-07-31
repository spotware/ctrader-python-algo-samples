import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartDragEventArgsSample():
    def initialize(self):
        api.Chart.DragStart += self.on_chart_drag_start
        api.Chart.Drag += self.on_chart_drag
        api.Chart.DragEnd += self.on_chart_drag_end
        
    def on_chart_drag_start(self, args):
        api.Print(f"Chart {args.Chart.SymbolName} {args.Chart.TimeFrame} Drag Started | Mouse Location: ({args.MouseX}, {args.MouseY})")

    def on_chart_drag_end(self, args):
        api.Print(f"Chart {args.Chart.SymbolName} {args.Chart.TimeFrame} Drag Ended | Mouse Location: ({args.MouseX}, {args.MouseY})")

    def on_chart_drag(self, args):
        api.Print(f"Chart {args.Chart.SymbolName} {args.Chart.TimeFrame} Dragging | Mouse Location: ({args.MouseX}, {args.MouseY})")