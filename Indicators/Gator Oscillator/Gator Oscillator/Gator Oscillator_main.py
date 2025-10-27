import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class GatorOscillator():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Indicators.MedianPrice(api.Bars).Result

        self.alligator = api.Indicators.Alligator(api.Source, api.JawsPeriods, api.JawsShift, api.TeethPeriods, api.TeethShift, api.LipsPeriods, api.LipsShift, api.MAType)
        
    def calculate(self, index):
        api.Upper[index] = abs(self.alligator.Jaws[index] - self.alligator.Teeth[index])
        api.Lower[index] = abs(self.alligator.Teeth[index] - self.alligator.Lips[index]) * -1

        api.SetLineAppearance(api.Upper.Line, index, api.UpColor if api.Upper[index] > api.Upper[index - 1] else api.DownColor)
        api.SetLineAppearance(api.Lower.Line, index, api.UpColor if api.Lower[index] < api.Lower[index - 1] else api.DownColor)
