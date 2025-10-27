import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MomentumOscillator():  
    def calculate(self, index):
        api.Result[index] = 100 * api.Source[index] / api.Source[index - api.Periods]