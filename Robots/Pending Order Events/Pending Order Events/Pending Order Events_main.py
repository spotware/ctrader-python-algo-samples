import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PendingOrderEvents():
    def on_start(self):
        api.PendingOrders.Cancelled += self.on_pending_orders_cancelled
        api.PendingOrders.Modified += self.on_pending_orders_modified
        api.PendingOrders.Filled += self.on_pending_orders_filled
        api.PendingOrders.Created += self.on_pending_orders_created

    def on_pending_orders_cancelled(self, args):
        cancelledOrder = args.PendingOrder
        cancellationReason = args.Reason
        api.Print(f"cancelledOrder: {cancelledOrder.Id} | cancellationReason: {cancellationReason}")

    def on_pending_orders_modified(self, args):
        modifiedOrder = args.PendingOrder
        api.Print(f"modifiedOrder: {modifiedOrder.Id}")

    def on_pending_orders_filled(self, args):
        pendingOrderThatFilled = args.PendingOrder
        filledPosition = args.Position
        api.Print(f"pendingOrderThatFilled: {pendingOrderThatFilled.Id} | filledPosition: {filledPosition.Id}")

    def on_pending_orders_created(self, args):
        createdOrder = args.PendingOrder
        api.Print(f"createdOrder: {createdOrder.Id}")