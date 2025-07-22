import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionBarsPassedSample():
    def on_start(self):
        currentIndex = api.Bars.Count - 1
        for position in api.Positions:
            if position.Label != api.Label:
                continue

            positionOpenBarIndex = api.Bars.OpenTimes.GetIndexByTime(position.EntryTime)
            numberOfBarsPassedSincePositionOpened = currentIndex - positionOpenBarIndex
            api.Print(numberOfBarsPassedSincePositionOpened)