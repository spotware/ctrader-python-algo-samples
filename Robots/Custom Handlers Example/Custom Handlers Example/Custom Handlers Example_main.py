import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class CustomHandlersExample():
    def on_start(self):
        api.Bars.BarOpened += self.on_bar_opened;

    def on_bar_opened(self, args):
        if api.Bars.LastBar.Open > api.Bars.Last(1).Close and api.Bars.LastBar.Open > api.Bars.Last(2).Close:
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, 10000, None, 10, 50)
        elif api.Bars.LastBar.Open < api.Bars.Last(1).Close and api.Bars.LastBar.Open < api.Bars.Last(2).Close:
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, 10000, None, 10, 50)
