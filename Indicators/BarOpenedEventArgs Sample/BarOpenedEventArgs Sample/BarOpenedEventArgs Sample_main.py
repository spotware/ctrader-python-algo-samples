import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BarOpenedEventArgsSample():
    def initialize(self):
        api.Bars.BarOpened += self.barOpened

    def barOpened(self, args):
        newOpendBar = args.Bars.LastBar
        # Or you can use args.Bars[Bars.Count - 1] or args.Bars.Last(0)
        closedBar = args.Bars.Last(1);
        api.Print(f"newOpendBar: {newOpendBar}")
        api.Print(f"closedBar: {closedBar}")