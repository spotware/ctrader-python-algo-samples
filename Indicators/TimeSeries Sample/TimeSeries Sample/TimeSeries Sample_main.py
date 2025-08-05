import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TimeSeriesSample():
    def initialize(self):
        # Every Bars object has a time series which is the open times of bars
        timeSeries = api.Bars.OpenTimes

        api.Print(f"Count: {timeSeries.Count}")

        # You can get another bars index by using TimeSeries GetIndexByTime/GetIndexByExactTime methods
        dailyBars = api.MarketData.GetBars(TimeFrame.Daily)
        dailyBarsIndex = timeSeries.GetIndexByTime(dailyBars.OpenTimes.LastValue)
        openPrice = api.Bars.OpenPrices[dailyBarsIndex]
        api.Print(f"Daily Bars Index: {dailyBarsIndex} | Open: {openPrice}")