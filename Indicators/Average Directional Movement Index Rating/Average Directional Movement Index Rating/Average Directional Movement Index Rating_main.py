import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AverageDirectionalMovementIndexRating():
    def initialize(self):
        self.dms = api.Indicators.DirectionalMovementSystem(api.Bars, api.Periods, api.MAType)
        
    def calculate(self, index):
        api.ADX[index] = self.dms.ADX[index]
        api.ADXR[index] = (self.dms.ADX[index] + self.dms.ADX[index - api.Periods]) / 2
        api.DIMinus[index] = self.dms.DIMinus[index]
        api.DIPlus[index] = self.dms.DIPlus[index]