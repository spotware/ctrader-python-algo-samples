import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import TimeSpan

class PendingOrderModificationSample():
    def on_start(self):
        order = None

        orders = []

        if len(api.OrderComment) > 0 and len(api.OrderLabel) > 0:
            orders = [o for o in api.PendingOrders if o.Comment == api.OrderComment and o.Lebel == api.OrderLabel]
        elif len(api.OrderComment) > 0:
            orders = [o for o in api.PendingOrders if o.Comment == api.OrderComment]
        elif len(api.OrderLabel) > 0:
            orders = [o for o in api.PendingOrders if o.Lebel == api.OrderLabel]

        if len(orders) == 0:
            api.Print("Couldn't find any matching order, please check the comment and label")
        else:
            for order in orders:
                self.modify_order(order)

        api.Stop()

    def modify_order(self, order):
        targetPrice = order.TargetPrice if api.TargetPrice == 0 else api.TargetPrice

        orderSymbol = api.Symbols.GetSymbol(order.SymbolName);

        stopLossInPips = order.StopLossPips if api.StopLossInPips == 0 else api.StopLossInPips
        takeProfitInPips = order.TakeProfitPips if api.TakeProfitInPips == 0 else api.TakeProfitInPips

        if len(api.Expiry) == 0:
            expiryTime = order.ExpirationTime
        elif api.Expiry == "0":
            expiryTime = None
        else:
            expiryTimeSpan = TimeSpan.Parse(api.Expiry)
            expiryTime = api.Server.Time.Add(expiryTimeSpan)

        volumeInUnits = order.VolumeInUnits if api.VolumeInLots == 0 else orderSymbol.QuantityToVolumeInUnits(api.VolumeInLots)

        if order.OrderType == PendingOrderType.Limit:
            api.ModifyPendingOrder(order, targetPrice, stopLossInPips, takeProfitInPips, expiryTime, volumeInUnits, api.HasTrailingStop, api.StopLossTriggerMethod)
        elif order.OrderType == PendingOrderType.Stop:
            api.ModifyPendingOrder(order, targetPrice, stopLossInPips, takeProfitInPips, expiryTime, volumeInUnits, api.HasTrailingStop, api.StopLossTriggerMethod, api.OrderTriggerMethod)
        elif order.OrderType == PendingOrderType.StopLimit:
            api.ModifyPendingOrder(order, targetPrice, stopLossInPips, takeProfitInPips, expiryTime, volumeInUnits, api.HasTrailingStop, api.StopLossTriggerMethod, api.OrderTriggerMethod, api.LimitRangeInPips)