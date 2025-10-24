import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AccumulativeSwingIndex():
    def initialize(self):
        self.swingIndexValues = api.Indicators.SwingIndex(api.LimitMoveValue)
     
    def calculate(self, index):
        api.Result[index] = self.swingIndexValues.Result[index] if index == 0 else self.swingIndexValues.Result[index - 1] + self.swingIndexValues.Result[index]
