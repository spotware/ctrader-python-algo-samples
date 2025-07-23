import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import Action

class TradeOperationSample():
    def on_start(self):
        tradeOperation = api.ExecuteMarketOrderAsync(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin, Action[TradeResult](self.on_trade_operation_completed))
        api.Print("Executing" if tradeOperation.IsExecuting else "Completed")

    def on_trade_operation_completed(self, trade_result):
        api.Print("Was Trade Operation Successful: ", trade_result.IsSuccessful)