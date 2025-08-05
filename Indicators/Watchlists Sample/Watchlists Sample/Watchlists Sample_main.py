import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WatchlistsSample():
    def initialize(self):
        api.Watchlists.Removed += self.on_watchlists_removed
        api.Watchlists.WatchlistRenamed += self.on_watchlists_renamed
        api.Watchlists.Added += self.on_watchlists_added
        api.Watchlists.WatchlistSymbolAdded += self.on_watchlists_symbol_added
        api.Watchlists.WatchlistSymbolRemoved += self.on_watchlists_symbol_removed

        api.Print(f"Number of Watchlists: {len(list(api.Watchlists))}")
        
        for watchlist in api.Watchlists:
            api.Print(f"Watchlist Name: {watchlist.Name} | Symbols #: {watchlist.SymbolNames.Count}")

    def on_watchlists_added(self, args):
        api.Print(f"Watchlist '{args.Watchlist.Name}' has been added")

    def on_watchlists_renamed(self, args):
        api.Print(f"Watchlist renamed to {args.Watchlist.Name}")

    def on_watchlists_removed(self, args):
        api.Print(f"Watchlist '{args.Watchlist.Name}' has been removed")        

    def on_watchlists_symbol_added(self, args):
        api.Print(f"Symbol {args.SymbolName} Added to Watchlist {args.Watchlist.Name}")

    def on_watchlists_symbol_removed(self, args):
        api.Print(f"Symbol {args.SymbolName} removed from watchlist {args.Watchlist.Name}")