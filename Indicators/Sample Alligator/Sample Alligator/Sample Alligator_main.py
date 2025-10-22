import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SampleAlligator():
    def initialize(self):
        self.jawsMa = api.Indicators.WellesWilderSmoothing(api.Bars.MedianPrices, api.JawsPeriods)
        self.teethMa = api.Indicators.WellesWilderSmoothing(api.Bars.MedianPrices, api.TeethPeriods)
        self.lipsMa = api.Indicators.WellesWilderSmoothing(api.Bars.MedianPrices, api.LipsPeriods)
        
    def calculate(self, index):
        api.Jaws[index + api.JawsShift] = self.jawsMa.Result[index]
        api.Teeth[index + api.TeethShift] = self.teethMa.Result[index]
        api.Lips[index + api.LipsShift] = self.lipsMa.Result[index]