import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Alligator():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Indicators.MedianPrice(Bars).Result

        self.jawsMa = api.Indicators.MovingAverage(api.Source, api.JawsPeriods, api.MAType)
        self.teethMa = api.Indicators.MovingAverage(api.Source, api.TeethPeriods, api.MAType)
        self.lipsMa = api.Indicators.MovingAverage(api.Source, api.LipsPeriods, api.MAType)
        
    def calculate(self, index):
        api.Jaws[index + api.JawsShift] = self.jawsMa.Result[index]
        api.Teeth[index + api.TeethShift] = self.teethMa.Result[index]
        api.Lips[index + api.LipsShift] = self.lipsMa.Result[index]