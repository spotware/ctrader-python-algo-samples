import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PatternsStrategySample():
    def on_bar_closed(self):
        if api.Bars.Last(0).Close == api.Bars.Last(0).High and (api.Bars.Last(0).Close - api.Bars.Last(0).Open) < (api.Bars.Last(0).Close - api.Bars.Last(0).Low) * 0.2:
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Volume, api.InstanceId, api.StopLoss, api.TakeProfit)

        if api.Bars.Last(0).Close == api.Bars.Last(0).Low and (api.Bars.Last(0).Open - api.Bars.Last(0).Close) < (api.Bars.Last(0).High - api.Bars.Last(0).Close) * 0.2:
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, api.Volume, api.InstanceId, api.StopLoss, api.TakeProfit)
