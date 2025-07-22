import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import TimeSpan, Action

class PendingOrderPlacingSample():
    def on_start(self):
        volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)

        distanceInPips = api.DistanceInPips * api.Symbol.PipSize

        stopLoss =  None if api.StopInPips == 0 else api.StopInPips
        takeProfit = None if api.TargetInPips == 0 else api.TargetInPips

        if len(api.Expiry) == 0 or api.Expiry == "0":
            expiryTime = None
        else:
            expiryTimeSpan = TimeSpan.Parse(api.Expiry)
            expiryTime = api.Server.Time.Add(expiryTimeSpan) if expiryTimeSpan.TotalMinutes > 0 else None

        on_completed_action = Action[TradeResult](self.on_order_completed)

        match api.OrderType:
            case PendingOrderType.Limit:
                limitPrice = api.Symbol.Ask - distanceInPips if api.OrderTradeType == TradeType.Buy else api.Symbol.Ask + distanceInPips

                if api.IsAsync:
                    api.PlaceLimitOrderAsync(api.OrderTradeType, api.SymbolName, volumeInUnits, limitPrice, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, on_completed_action)
                else:
                    result = api.PlaceLimitOrder(api.OrderTradeType, api.SymbolName, volumeInUnits, limitPrice, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod)
            case PendingOrderType.Stop:
                stopPrice = api.Symbol.Ask + distanceInPips if api.OrderTradeType == TradeType.Buy else api.Symbol.Ask - distanceInPips
      
                if api.IsAsync:
                    api.PlaceStopOrderAsync(api.OrderTradeType, api.SymbolName, volumeInUnits, stopPrice, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, api.StopOrderTriggerMethod, on_completed_action)
                else:
                    result = api.PlaceStopOrder(api.OrderTradeType, api.SymbolName, volumeInUnits, stopPrice, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, api.StopOrderTriggerMethod)
            case PendingOrderType.StopLimit:
                stopLimitPrice = api.Symbol.Ask + distanceInPips if api.OrderTradeType == TradeType.Buy else api.Symbol.Ask - distanceInPips
                if api.IsAsync:
                    api.PlaceStopLimitOrderAsync(api.OrderTradeType, api.SymbolName, volumeInUnits, stopLimitPrice, api.LimitRangeInPips, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, api.StopOrderTriggerMethod, on_completed_action)
                else:
                    result = api.PlaceStopLimitOrder(api.OrderTradeType, api.SymbolName, volumeInUnits, stopLimitPrice, api.LimitRangeInPips, api.Label, stopLoss, takeProfit, expiryTime, api.Comment, api.HasTrailingStop, api.StopLossTriggerMethod, api.StopOrderTriggerMethod)
            case _:
                api.Print("Invalid order type")

        if api.IsAsync == False:
            self.on_order_completed(result)

    def on_order_completed(self, result):
        if result.IsSuccessful == False:
            api.Print(f"Error: {result.Error}")
        api.Stop()