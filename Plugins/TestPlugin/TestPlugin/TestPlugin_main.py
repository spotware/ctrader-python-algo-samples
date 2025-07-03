import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TestPlugin():
    def on_start(self):
        api.Print("Plugin started!")
        # To learn more about cTrader Algo visit our Help Center:
        # https://help.ctrader.com/ctrader-algo/
        
    def on_stop(self):
        pass
