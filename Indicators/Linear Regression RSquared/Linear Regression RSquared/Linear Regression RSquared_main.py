import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LinearRegressionRSquared():
    def calculate(self, index):
        lastPoint = [(i + 1, api.Source[index - api.Periods + i + 1]) for i in range(api.Periods)]

        ex = sum([p[0] for p in lastPoint])
        ey = sum([p[1] for p in lastPoint])

        ex2 = sum([p[0] * p[0] for p in lastPoint])
        ey2 = sum([p[1] * p[1] for p in lastPoint])
        exy = sum([p[0] * p[1] for p in lastPoint])

        api.Result[index] = pow(exy * api.Periods - ex * ey, 2) / (ex2 * api.Periods - ex * ex) / (ey2 * api.Periods - ey * ey)