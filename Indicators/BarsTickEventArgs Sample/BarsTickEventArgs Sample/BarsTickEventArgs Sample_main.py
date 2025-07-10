import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BarsTickEventArgsSample():
    def initialize(self):
        api.Bars.Tick += self.barsTick

    def barsTick(self, args):
        api.Print(f"Last Close Price: {args.Bars.LastBar.Close} | Is new Bar: {args.IsBarOpened}")
