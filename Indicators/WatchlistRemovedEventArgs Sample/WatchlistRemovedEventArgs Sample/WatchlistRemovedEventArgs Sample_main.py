import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistRemovedEventArgsSample():
    def initialize(self):
        api.Watchlists.Removed += self.on_watchlists_removed

    def on_watchlists_removed(self, args):
        api.Print(f"Watchlist '{args.Watchlist.Name}' has been removed")