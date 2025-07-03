import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TestIndicator():
    def initialize(self):
        # Add your indicator initialization logic here
        api.Print("Indicator initialized")
        # To learn more about cTrader Algo visit our Help Center:
        # https://help.ctrader.com/ctrader-algo/
        
    def calculate(self, index):
        # Calculate indicator values here
        api.Result[index] = 100 # Example calculation