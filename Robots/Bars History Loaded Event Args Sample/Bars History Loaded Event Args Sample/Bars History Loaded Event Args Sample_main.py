import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class BarsHistoryLoadedEventArgsSample():
    def on_start(self):
        api.Bars.HistoryLoaded += self.on_bars_history_loaded

        # You can load more bars by calling this method or LoadMoreHistory
        api.Bars.LoadMoreHistoryAsync()
    
    def on_bars_history_loaded(self, args):
        api.Print(f"Loaded Bars Count: {args.Count}");