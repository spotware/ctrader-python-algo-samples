import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class BarOpenedExample():
    def on_bar(self):
        previousBar = api.Bars[api.Bars.Count - 2]
        priceDifference = ((api.Bars.LastBar.Open - previousBar.Open) / previousBar.Open) * 100

        if priceDifference > 0.2:
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin)
        elif priceDifference < -0.2:
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, api.Symbol.VolumeInUnitsMin)
        else:
            for position in api.Positions:
                position.Close()