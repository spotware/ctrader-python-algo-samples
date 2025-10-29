import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TickVolume():
    def calculate(self, index):
        outputIndex = index + api.Shift
        api.Result[outputIndex] = api.Bars.TickVolumes[index]