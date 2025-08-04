import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import Double
from math import nan

class MarketDepthSample():
    def initialize(self):
        self.marketDepth = api.MarketData.GetMarketDepth(api.SymbolName)
        self.marketDepth.Updated += self.on_market_depth_updated

    def on_market_depth_updated(self):
        self.askNo = 0
        self.bidNo = 0

        index = api.Bars.ClosePrices.Count - 1

        for i in range(self.marketDepth.AskEntries.Count):
            api.AskResult[index - i] = nan
            
        for entry in self.marketDepth.AskEntries:
            api.AskResult[index - self.askNo] = (-1) * entry.VolumeInUnits
            self.askNo += 1

        for i in range(self.marketDepth.BidEntries.Count):
            api.BidResult[index - i] = nan

        for entry in self.marketDepth.BidEntries:
            api.BidResult[index - self.bidNo] = entry.VolumeInUnits
            self.bidNo += 1