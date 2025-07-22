import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System.Threading import Thread

class RefreshDataSample():
    def on_start(self):
        execututionResults = []

        for i in range(50):
            execututionResults.append(api.ExecuteMarketOrderAsync(TradeType.Buy if i % 2 == 0 else TradeType.Sell, api.SymbolName, api.Symbol.VolumeInUnitsMin))

        api.Print("All orders sent");

        while self.is_any_executing(execututionResults):
            api.Print("Waiting...")
            Thread.Sleep(100)
            # If you remove the RefreshData method call
            # cBot main thread will stuck and the rest
            # of the code will not be executed
            api.RefreshData()

        api.Print("Closing Positions");

        for position in api.Positions:
            if position.TradeType == TradeType.Sell:
                continue
            api.ClosePositionAsync(position)

    def is_any_executing(self, results):
        for result in results:
            if result.IsExecuting:
                return True
        return False