import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PositionCurrentPriceSample():
    def initialize(self):
        # Opening a new position on start
        api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, 10000, "indicator sample")   
        # Storing the new position in the variable
        self.indicatorPosition = api.Positions.Find("indicator sample")

    def calculate(self, index):
        # Assigning the percentile difference between
        # the entry price and the current price to the indicator output
        api.Result[index] = ((self.indicatorPosition.CurrentPrice - self.indicatorPosition.EntryPrice) / self.indicatorPosition.EntryPrice) * 100