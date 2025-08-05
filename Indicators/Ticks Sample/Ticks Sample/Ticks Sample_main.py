import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TicksSample():
    def initialize(self):
        # Getting a symbol ticks data
        self.ticks = api.MarketData.GetTicks(api.InputSymbolName)
        # Subscribing to upcoming ticks
        self.ticks.Tick += self.on_ticks_tick

        self.ticks.HistoryLoaded += self.on_ticks_history_loaded
        # You can also pass a callback method instead of subscribing to HistoryLoaded event
        self.ticks.LoadMoreHistoryAsync();
        self.ticks.Reloaded += self.on_ticks_reloaded
    
    def on_ticks_tick(self, args):
        api.Print(str(args.Ticks.LastTick))

    def on_ticks_history_loaded(self, args):
        api.Print(f"New ticks loaded: #{args.Count}")

    def on_ticks_reloaded(self, args):
        api.Print("Ticks got reloaded")