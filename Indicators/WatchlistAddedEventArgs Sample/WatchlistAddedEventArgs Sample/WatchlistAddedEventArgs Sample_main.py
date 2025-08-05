import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistAddedEventArgsSample():
    def initialize(self):
        api.Watchlists.Added += self.on_watchlists_added

    def on_watchlists_added(self, args):
        api.Print(f"Watchlist '{args.Watchlist.Name}' has been added")