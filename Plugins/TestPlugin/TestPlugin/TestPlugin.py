import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TestPlugin():
    def OnStart(self):
        api.Print("Plugin started!")
        # To learn more about cTrader Algo visit our Help Center:
        # https://help.ctrader.com/ctrader-algo/
        
    def OnStop(self):
        pass
