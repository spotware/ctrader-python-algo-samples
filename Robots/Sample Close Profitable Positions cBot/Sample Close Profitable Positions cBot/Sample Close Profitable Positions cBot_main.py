import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleCloseProfitablePositionscBot():
    def on_start(self):
        for position in api.Positions:
            if position.GrossProfit > 0:
                api.ClosePosition(position)