import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SymbolTickEventArgsSample():
    def initialize(self):
        api.Symbol.Tick += self.on_symbol_tick

    def on_symbol_tick(self, args):
        api.Print(f"Symbol: {args.SymbolName} | Ask: {args.Ask} | Bid: {args.Bid}")