import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import Int32

class AddIndicatorSample():
    def on_start(self):
        self.fastMaIndicator = api.Chart.Indicators.Add("Simple Moving Average", api.SourceSeries, Int32(api.FastPeriods))
        self.slowMaIndicator = api.Chart.Indicators.Add("Simple Moving Average", api.SourceSeries, Int32(api.SlowPeriods))

        self.fastMaIndicator.Lines[0].Color = Color.Red
        self.fastMaIndicator.Lines[0].Thickness = 3

        self.slowMaIndicator.Lines[0].Color = Color.Yellow
        self.slowMaIndicator.Lines[0].Thickness = 2

    def on_bar_closed(self):
        api.Chart.Indicators.Remove(self.fastMaIndicator)
        api.Chart.Indicators.Remove(self.slowMaIndicator)
