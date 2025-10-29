import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class OnBalanceVolume():
    def calculate(self, index):
        outputIndex = index + api.Shift

        if index == 0:
            api.Result[outputIndex] = 1
            return

        if api.Source[index] > api.Source[index - 1]:
            api.Result[outputIndex] = api.Result[outputIndex - 1] + api.Bars.TickVolumes[index]
        elif api.Source[index] < api.Source[index - 1]:
            api.Result[outputIndex] = api.Result[outputIndex - 1] - api.Bars.TickVolumes[index]
        else:
            api.Result[outputIndex] = api.Result[outputIndex - 1]