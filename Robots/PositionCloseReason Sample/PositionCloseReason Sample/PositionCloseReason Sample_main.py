import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionCloseReasonSample():
    def on_start(self):
        api.Positions.Closed += self.on_position_closed

    def on_position_closed(self, args):
        api.Print(args.Reason)
        match args.Reason:
            case PositionCloseReason.Closed:
                # Do something if position closed
                pass
            case PositionCloseReason.StopLoss:
                # Do something if position stop loss got hit
                pass
            case PositionCloseReason.StopOut:
                # Do something if position stopped out
                pass
            case PositionCloseReason.TakeProfit:
                # Do something if position take profit got hit
                pass