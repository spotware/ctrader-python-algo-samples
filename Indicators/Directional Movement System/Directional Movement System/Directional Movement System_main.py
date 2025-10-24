import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class DirectionalMovementSystem():
    def initialize(self):
        self.trueRange = api.Indicators.TrueRange()
        self.trueRangeAverage = api.Indicators.MovingAverage(self.trueRange.Result, api.Periods, api.MAType)

        self.upDmi = api.CreateDataSeries()
        self.downDmi = api.CreateDataSeries()

        self.upDmiMa = api.Indicators.MovingAverage(self.upDmi, api.Periods, api.MAType)
        self.downDmiMa = api.Indicators.MovingAverage(self.downDmi, api.Periods, api.MAType)

        self.dx = api.CreateDataSeries()
        self.averageDx = api.Indicators.MovingAverage(self.dx, api.Periods, api.MAType)
        
    def calculate(self, index):
        high = api.Bars.HighPrices[index]
        previousHigh = api.Bars.HighPrices[index - 1]

        low = api.Bars.LowPrices[index]
        previousLow = api.Bars.LowPrices[index - 1]

        upMove = high - previousHigh
        downMove = previousLow - low

        if upMove > downMove and upMove > 0:
            self.upDmi[index] = upMove
        else:
            self.upDmi[index] = 0

        if downMove > upMove and downMove > 0:
            self.downDmi[index] = downMove
        else:
            self.downDmi[index] = 0

        trueRange = self.trueRangeAverage.Result[index]

        diPlus = 100 * self.upDmiMa.Result[index] / trueRange
        diMinus = 100 * self.downDmiMa.Result[index] / trueRange

        api.DIPlus[index] = diPlus
        api.DIMinus[index] = diMinus

        absDifference = abs(diPlus - diMinus)
        diSum = diPlus + diMinus

        self.dx[index] = 100 * absDifference / diSum if diSum > 0 else float("nan") if math.isnan(diSum) else 0

        api.ADX[index] = self.averageDx.Result[index]