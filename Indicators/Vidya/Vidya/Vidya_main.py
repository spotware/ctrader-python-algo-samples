import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class Vidya():
    def calculate(self, index):
        prevResult = api.Result[index - 1]

        if math.isnan(prevResult):
            prevResult = api.Price[index - 1]

        k = api.Sigma * self.cmo(index)
        api.Result[index] = (1 - k) * prevResult + k * api.Price[index]

    def cmo(self, index):
        sumUp = 0
        sumDown = 0

        for i in range(api.Periods):
            difference = api.Price[index - i] - api.Price[index - i - 1]

            if difference > 0:
                sumUp += difference;
            else:
                sumDown += -difference;

        if sumUp + sumDown == 0:
            return 0.0

        return abs((sumUp - sumDown) / (sumUp + sumDown))