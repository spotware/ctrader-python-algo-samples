import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PriceVolumeTrend():
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index == 0:
            api.Result[outputIndex] = 0
            return;

        api.Result[outputIndex] = api.Result[outputIndex - 1] + api.Bars.TickVolumes[index] * (api.Source[index] - api.Source[index - 1]) / api.Source[index - 1]