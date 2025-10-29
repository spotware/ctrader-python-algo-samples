import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class RelativeStrengthIndex():
    def initialize(self):
        self.gains = api.CreateDataSeries()
        self.losses = api.CreateDataSeries()
        
        emaPeriods = 2 * api.Periods - 1

        self.exponentialMovingAverageGain = api.Indicators.MovingAverage(self.gains, emaPeriods, MovingAverageType.Exponential)
        self.exponentialMovingAverageLoss = api.Indicators.MovingAverage(self.losses, emaPeriods, MovingAverageType.Exponential)
        
    def calculate(self, index):
        currentValue = api.Source[index]
        previousValue = api.Source[index - 1]

        if currentValue > previousValue:
            self.gains[index] = currentValue - previousValue
            self.losses[index] = 0.0
        elif currentValue < previousValue:
            self.gains[index] = 0.0
            self.losses[index] = previousValue - currentValue
        else:
            self.gains[index] = 0.0
            self.losses[index] = 0.0

        relativeStrength = self.exponentialMovingAverageGain.Result[index] / self.exponentialMovingAverageLoss.Result[index]

        api.Result[index] = 100 - 100 / (1 + relativeStrength)