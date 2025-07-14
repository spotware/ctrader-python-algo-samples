import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class BarClosedExample():
    def on_bar_closed(self):
        lowCloseDifference = ((api.Bars.LastBar.Close - api.Bars.LastBar.Low) / api.Bars.LastBar.Close) * 100

        if lowCloseDifference <= 0.2:
            return

        for position in api.Positions:
            position.Close()

        api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin, None, None, 50)