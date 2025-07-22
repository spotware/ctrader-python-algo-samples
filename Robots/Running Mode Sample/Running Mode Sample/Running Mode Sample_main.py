import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class RunningModeSample():
    def on_start(self):
        api.Print(api.RunningMode)
        match api.RunningMode:
            case RunningMode.RealTime:
                # If the robot is running on real time market condition
                pass
            case RunningMode.SilentBacktesting:
                # If the robot is running on backtest and the visual mode is off
                pass
            case RunningMode.VisualBacktesting:
                # If the robot is running on backtest and the visual mode is on
                pass
            case RunningMode.Optimization:
                # If the robot is running on optimizer
                pass