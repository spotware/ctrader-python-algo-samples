import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class TradeResultSample():
    def on_start(self):
        tradeResult = api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin)

        if tradeResult.IsSuccessful:
            api.Print("Market order execution was successful")

            position = tradeResult.Position;

            api.Print(f"A new position opend with ID: {position.Id} ")
        else:
            Print(f"Market order execution was not successful: {tradeResult.Error}")