import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class HighMinusLow():
    def calculate(self, index):
        api.Result[index + api.Shift] = round(api.Bars.HighPrices[index] - api.Bars.LowPrices[index], api.Symbol.Digits)