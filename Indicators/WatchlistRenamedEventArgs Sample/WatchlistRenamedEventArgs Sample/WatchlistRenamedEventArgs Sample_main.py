import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistRenamedEventArgsSample():
    def initialize(self):
        api.Watchlists.WatchlistRenamed += self.on_watchlists_renamed

    def on_watchlists_renamed(self, args):
        api.Print(f"Watchlist renamed to {args.Watchlist.Name}")