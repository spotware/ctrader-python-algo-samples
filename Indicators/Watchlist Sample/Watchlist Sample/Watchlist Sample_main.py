import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistSample():
    def initialize(self):
        api.Print(f"Number of Watchlists: {len(list(api.Watchlists))}")

        for watchlist in api.Watchlists:
            api.Print(f"Watchlist Name: {watchlist.Name} | Symbols #: {watchlist.SymbolNames.Count}")