import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

class TestRobot():
    def OnStart(self):
        api.Print("Robot started!")
        # To learn more about cTrader Algo visit our Help Center:
        # https://help.ctrader.com/ctrader-algo/

    def OnTick(self):
        # Handle price updates here
        pass

    def OnStop(self):
        # Handle cBot stop here
        pass