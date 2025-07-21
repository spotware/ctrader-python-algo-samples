import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PendingOrderCancelationSample():
    def on_start(self):
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
                api.CancelPendingOrder(order)
        
        api.Stop()