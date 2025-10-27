import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LinearRegressionSlope():
    def calculate(self, index):
        if index <= api.Periods:
            return

        ex = 0
        ey = 0
        ex2 = 0
        exy = 0

        for i in range(api.Periods):
            x = i + 1
            y = api.Source[index - api.Periods + i + 1]

            ex += x
            ey += y
            ex2 += x * x
            exy += x * y

        api.Result[index] = (exy * api.Periods - ex * ey) / (ex2 * api.Periods - pow(ex, 2))