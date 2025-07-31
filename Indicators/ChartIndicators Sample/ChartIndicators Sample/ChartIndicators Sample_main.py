import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import Int32

class ChartIndicatorsSample():
    def initialize(self):
        # Adding the two SMAs on indicator start
        self.slow_sma = api.ChartIndicators.Add("Simple Moving Average", "Close", Int32(50))
        self.fast_sma = api.ChartIndicators.Add("Simple Moving Average", "Close", Int32(20))
            
        # Initialising the indicator from which the ADX value will be taken
        self.averageDirectionalMovementIndexRating = api.Indicators.AverageDirectionalMovementIndexRating(20)
        
    def calculate(self, index):
        if api.IsLastBar == False:
            return
        # Accessing and comparing the ADX value to 30
        if self.averageDirectionalMovementIndexRating.ADX[index] > 30:
            # Setting the SMA line properties
            self.fast_sma.Lines[0].Color = Color.Green
            self.fast_sma.Lines[0].Thickness = 3
            self.slow_sma.Lines[0].Color = Color.Blue
            self.slow_sma.Lines[0].Thickness = 3
        else:
            # Setting the SMA line properties
            self.fast_sma.Lines[0].Color = Color.Orange
            self.fast_sma.Lines[0].Thickness = 3
            self.slow_sma.Lines[0].Color = Color.Purple
            self.slow_sma.Lines[0].Thickness = 3