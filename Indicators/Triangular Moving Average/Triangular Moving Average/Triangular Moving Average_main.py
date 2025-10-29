import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TriangularMovingAverage():
    def initialize(self):
        self.movingAverageOverSource = api.Indicators.MovingAverage(api.Source, api.Periods, MovingAverageType.Simple)
        self.movingAverageOverMovingAverage = api.Indicators.MovingAverage(self.movingAverageOverSource.Result, api.Periods, MovingAverageType.Simple)
        
    def calculate(self, index):
        api.Result[index + api.Shift] = self.movingAverageOverMovingAverage.Result[index]