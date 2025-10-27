import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class EaseOfMovement():
    def initialize(self):
        self.notSmoothedEaseOfMovement = api.CreateDataSeries()
        self.movingAverage = api.Indicators.MovingAverage(self.notSmoothedEaseOfMovement, api.Periods, api.MAType)
        
    def calculate(self, index):
        if index < 2:
            return

        high = api.Bars.HighPrices[index]
        low = api.Bars.LowPrices[index]
        prevHigh = api.Bars.HighPrices[index - 1]
        prevLow = api.Bars.LowPrices[index - 1]
        tickVolume = api.Bars.TickVolumes[index]

        distanceMoved = (high + low) / 2 - (prevHigh + prevLow) / 2

        emv = 0

        if high != low:
            emv = distanceMoved / (tickVolume / (high - low))

        self.notSmoothedEaseOfMovement[index] = emv * 10000

        api.Result[index + api.Shift] = self.movingAverage.Result[index]