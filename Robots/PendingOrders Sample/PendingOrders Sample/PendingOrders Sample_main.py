import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PendingOrdersSample():
    def on_start(self):
        api.PendingOrders.Cancelled += self.on_pending_order_cancelled
        api.PendingOrders.Created += self.on_pending_order_created
        api.PendingOrders.Modified += self.on_pending_order_modified
        api.PendingOrders.Filled += self.on_pending_order_filled

        orders = [order for order in api.PendingOrders if order.Label == api.Label]

        # Getting orders target prices
        ordersTargetPrices = [order.TargetPrice for order in orders]

        # Getting orders symbols
        orderSymbols = [api.Symbols.GetSymbol(order.SymbolName) for order in orders]

    def on_pending_order_cancelled(self, args):
        api.Print(f"Order Cancelled: {args.PendingOrder.Id}")

    def on_pending_order_created(self, args):
        api.Print(f"Order Created: {args.PendingOrder.Id}")

    def on_pending_order_modified(self, args):
        api.Print(f"Order Modified: {args.PendingOrder.Id}")

    def on_pending_order_filled(self, args):
        api.Print(f"Order Filled: {args.PendingOrder.Id}")