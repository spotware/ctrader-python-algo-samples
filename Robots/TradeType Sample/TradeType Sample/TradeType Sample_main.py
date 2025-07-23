import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class TradeTypeSample():
    def on_start(self):
        api.ExecuteMarketOrder(api.TradeType, api.SymbolName, api.Symbol.VolumeInUnitsMin)