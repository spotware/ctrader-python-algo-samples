import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class StopTriggerMethodSample():
    def on_start(self):
        # Setting a new position StopTriggerMethod
        api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin, "StopTriggerMethod Test", 10, 10, "", False, api.StopTriggerMethod)

        # Setting a new stop order StopTriggerMethod for both order and its stop loss
        target = api.Symbol.Bid + (100 * api.Symbol.PipSize)

        api.PlaceStopOrder(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin, target, "StopTriggerMethod Test", 10, 10, None, "", False, api.StopTriggerMethod, api.StopTriggerMethod)

        # Changing open positions StopTriggerMethod
        for position in api.Positions:
            if position.StopLoss is None:
                continue

            api.ModifyPosition(position, position.StopLoss, position.TakeProfit, position.HasTrailingStop, api.StopTriggerMethod)

        # Changing open pending orders (Stop and StopLimit) StopTriggerMethod
        for order in api.PendingOrders:
            if order.StopLossPips is None or order.OrderType == PendingOrderType.Limit:
                continue

            api.ModifyPendingOrder(order, order.TargetPrice, order.StopLossPips, order.TakeProfitPips, order.ExpirationTime, order.VolumeInUnits, order.HasTrailingStop, api.StopTriggerMethod, api.StopTriggerMethod)