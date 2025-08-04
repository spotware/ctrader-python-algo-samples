import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MarketDataSample():
    def initialize(self):
        symbol = api.Symbol if api.UseCurrentSymbol else api.Symbols.GetSymbol(api.OtherSymbolName)
        timeframe = api.TimeFrame if api.UseCurrentTimeFrame else api.OtherTimeFrame

        # You can use GetBarsAsync instead of GetBars
        self.bars = api.MarketData.GetBars(timeframe, symbol.Name)
        # You can use GetTicksAsync instead of GetTicks
        self.ticks = api.MarketData.GetTicks(symbol.Name)
        # Getting market depth data
        self.marketDepth = api.MarketData.GetMarketDepth(symbol.Name)