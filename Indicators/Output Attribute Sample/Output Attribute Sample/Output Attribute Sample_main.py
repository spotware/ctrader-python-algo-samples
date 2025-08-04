import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class OutputAttributeSample():
    def calculate(self, index):
        api.OpenOutput[index] = api.Bars.OpenPrices[index]
        api.HighOutput[index] = api.Bars.HighPrices[index]
        api.LowOutput[index] = api.Bars.LowPrices[index]
        api.CloseOutput[index] = api.Bars.ClosePrices[index]