import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ErrorSample():
    def on_start(self):
        # We use 0 for volume to cause an error
        tradeResult = api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, 0);

        if tradeResult.IsSuccessful == False:
            api.Print(tradeResult.Error)
            api.Stop()