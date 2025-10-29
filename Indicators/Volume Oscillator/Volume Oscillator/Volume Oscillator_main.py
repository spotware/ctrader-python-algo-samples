import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class VolumeOscillator():
    def initialize(self):
        self.fastMovingAverage = api.Indicators.MovingAverage(api.Bars.TickVolumes, api.ShortTerm, MovingAverageType.Simple);
        self.slowMovingAverage = api.Indicators.MovingAverage(api.Bars.TickVolumes, api.LongTerm, MovingAverageType.Simple);
        
    def calculate(self, index):
        api.Result[index + api.Shift] = self.fastMovingAverage.Result[index] - self.slowMovingAverage.Result[index]