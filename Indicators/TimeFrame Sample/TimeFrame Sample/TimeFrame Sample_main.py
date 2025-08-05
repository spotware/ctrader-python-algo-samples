import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TimeFrameSample():
    def initialize(self):
        api.Print(f"Name: {api.UserSelectedTimeFrame.Name} | Short Name: {api.UserSelectedTimeFrame.ShortName}")
        # Getting another time frame bars data, using user selected time frame
        barsBasedOnUserSelectedTimeFrame = api.MarketData.GetBars(api.UserSelectedTimeFrame)
        # Getting another time frame bars data, using pre-defined TimeFrames
        barsBasedOnOtherTimeFrame = api.MarketData.GetBars(TimeFrame.Day2)