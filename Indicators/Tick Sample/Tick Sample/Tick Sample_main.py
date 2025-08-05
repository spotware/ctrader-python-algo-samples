import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TickSample():
    def initialize(self):
        # Getting a symbol ticks data
        self.ticks = api.MarketData.GetTicks(api.InputSymbolName)
        # Subscribing to upcoming ticks
        self.ticks.Tick += self.on_tick
    
    def on_tick(self, args):
        # Printing Last tick inside Ticks collection
        api.Print(f"Bid: {args.Ticks.LastTick.Bid} | Ask: {args.Ticks.LastTick.Ask} | Time: {args.Ticks.LastTick.Time.ToString("dd/MM/yyyy HH:mm:ss")}")