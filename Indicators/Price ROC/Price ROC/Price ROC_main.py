import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PriceROC(): 
    def calculate(self, index):
        api.Result[index] = (api.Source[index] - api.Source[index - api.Periods]) / api.Source[index - api.Periods] * 100