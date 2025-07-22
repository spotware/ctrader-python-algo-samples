import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import Action

class PositionExecutionSample():
    def on_start(self):
        volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        distanceInPips = api.DistanceInPips * api.Symbol.PipSize

        stopLoss = None if api.StopInPips == 0 else api.StopInPips
        takeProfit = None if api.TargetInPips == 0 else api.TargetInPips

        on_completed_action = Action[TradeResult](self.on_completed)

        if api.IsAsync:
            api.ExecuteMarketOrderAsync(api.Direction, api.SymbolName, volumeInUnits, api.Label, stopLoss, takeProfit, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, on_completed_action)
        else:
            result = api.ExecuteMarketOrder(api.Direction, api.SymbolName, volumeInUnits, api.Label, stopLoss, takeProfit, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod)

        if api.IsAsync == False:
            self.on_completed(result)

    def on_completed(self, result):
        if result.IsSuccessful == False:
            api.Print(f"Error: {result.Error}")
        
        api.Stop()