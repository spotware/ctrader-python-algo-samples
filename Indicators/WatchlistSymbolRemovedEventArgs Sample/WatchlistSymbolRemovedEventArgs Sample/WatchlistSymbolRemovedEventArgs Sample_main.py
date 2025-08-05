import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistSymbolRemovedEventArgsSample():
    def initialize(self):
        api.Watchlists.WatchlistSymbolRemoved += self.on_watchlists_symbol_removed

    def on_watchlists_symbol_removed(self, args):
        api.Print(f"Symbol {args.SymbolName} removed from watchlist {args.Watchlist.Name}")