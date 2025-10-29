import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class VariableIndexDynamicAverage():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Bars.ClosePrices

        self.cmo = api.Indicators.ChandeMomentumOscillator(api.Source, api.CMOPeriods)
        self.smoothingFactor = 2 / (api.SmoothPeriods + 1)
        
    def calculate(self, index):
        prevResult = api.Result[index - 1]

        if math.isnan(prevResult):
            prevResult = api.Source[index - 1]

        absCmo = abs(self.cmo.Result[index]) / 100
        api.Result[index] = api.Source[index] * absCmo * self.smoothingFactor + prevResult * (1 - self.smoothingFactor * absCmo)