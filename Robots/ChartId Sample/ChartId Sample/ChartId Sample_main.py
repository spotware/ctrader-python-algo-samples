import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ChartIdSample():
    def on_start(self):
        api.Print(f"Current bot chart Id is: {api.Chart.Id}")