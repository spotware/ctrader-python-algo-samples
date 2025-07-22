import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionCurrentPriceSample():
    def on_start(self):
        api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin, "cbot position")

    def on_bar_closed(self):
        # Finding all positions opened by the cBot
        cbotPositions = api.Positions.FindAll("cbot position")
            
        # Iterating over all positions opened by the cBot
        for position in cbotPositions:
            if position.CurrentPrice > position.EntryPrice:
                # Placing a limit order in the opposite direction
                # and above the current price if the current price
                # is greater than the entry price
                api.PlaceLimitOrder(TradeType.Sell, api.SymbolName, api.Symbol.VolumeInUnitsMin * 2, position.CurrentPrice * 1.05, "cbot position");
            else:
                position.Close();           
                # Placing a limit order in the opposite direction
                # and below the current price if the current price
                # is smaller than the entry price
                api.PlaceLimitOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin * 2, position.CurrentPrice * 0.95, "cbot position");