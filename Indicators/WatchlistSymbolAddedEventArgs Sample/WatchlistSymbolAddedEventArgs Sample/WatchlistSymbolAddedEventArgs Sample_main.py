import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistSymbolAddedEventArgsSample():
    def initialize(self):
        api.Watchlists.WatchlistSymbolAdded += self.on_watchlists_symbol_added

    def on_watchlists_symbol_added(self, args):
        api.Print(f"Symbol {args.SymbolName} Added to Watchlist {args.Watchlist.Name}")