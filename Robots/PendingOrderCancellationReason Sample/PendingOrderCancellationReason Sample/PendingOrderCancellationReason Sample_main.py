import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PendingOrderCancellationReasonSample():
    def on_start(self):
        api.PendingOrders.Cancelled += self.on_pending_order_cancelled

    def on_pending_order_cancelled(self, args):
        api.Print(args.Reason);
        match args.Reason:
            case PendingOrderCancellationReason.Cancelled:
                # Do something if order cancelled
                pass
            case PendingOrderCancellationReason.Expired:
                # Do something if order expired
                pass
            case PendingOrderCancellationReason.Rejected:
                # Do something if order rejected
                pass
