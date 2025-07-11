import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class AddToChartSample():
    def on_start(self):
        self.macd = api.Indicators.MacdCrossOver(26, 19, 9)
        self.rsi = api.Indicators.RelativeStrengthIndex(api.Bars.ClosePrices, 9)
            
        self.rsi.AddToChart()
        self.macd.AddToChart()

    def on_bar_closed(self):
        if self.macd.Histogram.LastValue > 0 and self.rsi.Result.LastValue <= 30:
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, 10000)
        elif (self.macd.Histogram.LastValue < 0 and self.rsi.Result.LastValue >= 70):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, 10000)
    
    def close_positions(self, tradeType):
        for position in api.Positions:
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)
             
