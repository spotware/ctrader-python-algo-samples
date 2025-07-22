import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class RangeStrategyExample():
    def on_bar_closed(self):
        if api.Bars.Last(0).Close > api.Bars.Last(0).Open and api.Bars.Last(1).Close < api.Bars.Last(1).Open and api.Bars.Last(0).Close > api.Bars.Last(1).Open:
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Volume, api.InstanceId, api.StopLoss, api.TakeProfit)
        
        if api.Bars.Last(0).Close < api.Bars.Last(0).Open and api.Bars.Last(1).Close > api.Bars.Last(1).Open and api.Bars.Last(0).Close < api.Bars.Last(1).Open:
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, api.Volume, api.InstanceId, api.StopLoss, api.TakeProfit)