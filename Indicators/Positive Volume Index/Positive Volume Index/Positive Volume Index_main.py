import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PositiveVolumeIndex():
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index == 0:
            api.Result[outputIndex] = 1
            return

        if api.Bars.TickVolumes[index] <= api.Bars.TickVolumes[index - 1]:
            api.Result[outputIndex] = api.Result[outputIndex - 1]
        else:
            api.Result[outputIndex] = api.Result[outputIndex - 1] + (api.Source[index] - api.Source[index - 1]) / api.Source[index - 1] * api.Result[outputIndex - 1]