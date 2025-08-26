import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import Int64

class BarsOutputSample():
    def initialize(self):
        self.openEma = api.Indicators.ExponentialMovingAverage(api.Bars.OpenPrices, api.EmaPeriods)
        self.highEma = api.Indicators.ExponentialMovingAverage(api.Bars.HighPrices, api.EmaPeriods)
        self.lowEma = api.Indicators.ExponentialMovingAverage(api.Bars.LowPrices, api.EmaPeriods)
        self.closeEma = api.Indicators.ExponentialMovingAverage(api.Bars.ClosePrices, api.EmaPeriods)

        # You can hide main chart bars
        # api.Chart.DisplaySettings.Bars = False

        # You can change output colors and other appearance properties via code
        # api.Result.Output.BullFillColor = Color.Blue
        # api.Result.Output.BullOutlineColor = Color.Blue
        # api.Result.Output.BearFillColor = Color.Gold
        # api.Result.Output.BearOutlineColor = Color.Gold
        # api.Result.Output.ChartType = ChartType.Bars
        # api.Result.Output.TickVolumeColor = Color.Magenta
        
    def calculate(self, index):
        api.Result[index] = OhlcvBar(self.openEma.Result[index], self.highEma.Result[index], self.lowEma.Result[index], self.closeEma.Result[index], int(api.Bars.TickVolumes[index]))
        # You can set custom colors for each bar by using SetBarColor
        # if index % 2 == 0:
        #   api.SetBarColor(api.Result.Output, index, Color.Yellow, Color.White, Color.Green)