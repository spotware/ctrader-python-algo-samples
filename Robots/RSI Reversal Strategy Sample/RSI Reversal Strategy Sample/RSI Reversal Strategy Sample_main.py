import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class RSIReversalStrategySample():
    def on_start(self):
        self.rsi = api.Indicators.RelativeStrengthIndex(api.Bars.ClosePrices, 14)

    def on_bar_closed(self):
        if self.rsi.Result.LastValue < api.BuyLevel:
            if api.Positions.Count == 0:
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin)
            self.close_positions(TradeType.Sell)        
        elif self.rsi.Result.LastValue > api.SellLevel:
            if api.Positions.Count == 0:
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, api.Symbol.VolumeInUnitsMin);
            self.close_positions(TradeType.Buy)    

    def close_positions(self, tradeType):
        for position in api.Positions:
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)