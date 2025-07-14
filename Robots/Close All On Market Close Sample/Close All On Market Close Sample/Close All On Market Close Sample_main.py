import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

from datetime import timedelta

# Import trading wrapper functions
from robot_wrapper import *

class CloseAllOnMarketCloseSample():
    def on_start(self):
        closeBeforeTimeSplit = api.CloseBeforeTime.split(":")
        self.closeBeforeTime = timedelta(hours=int(closeBeforeTimeSplit[0]), minutes=int(closeBeforeTimeSplit[1]), seconds=int(closeBeforeTimeSplit[2]))
        api.Timer.Start(1)

    def on_timer(self):
        timeTillClose = api.Symbol.MarketHours.TimeTillClose();
        timeTillCloseDelta = timedelta(hours=timeTillClose.Hours, minutes=timeTillClose.Minutes, seconds=timeTillClose.Seconds)

        if api.Symbol.MarketHours.IsOpened() == False or timeTillCloseDelta > self.closeBeforeTime:
            return

        for position in api.Positions:
            api.ClosePosition(position)
