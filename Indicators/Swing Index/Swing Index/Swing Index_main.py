import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SwingIndex():        
    def calculate(self, index):
        o2 = api.Bars.OpenPrices[index]
        h2 = api.Bars.HighPrices[index]
        l2 = api.Bars.LowPrices[index]
        c2 = api.Bars.ClosePrices[index]

        o1 = api.Bars.OpenPrices[index - 1]
        c1 = api.Bars.ClosePrices[index - 1]

        h2c1 = abs(h2 - c1)
        l2c1 = abs(l2 - c1)
        h2l2 = abs(h2 - l2)
        c1o1 = abs(c1 - o1)

        if h2c1 > l2c1 and h2c1 > h2l2:
            r = h2c1 - 0.5 * l2c1 + 0.25 * c1o1
        elif l2c1 > h2c1 and l2c1 > h2l2:
            r = l2c1 - 0.5 * h2c1 + 0.25 * c1o1
        elif h2l2 > h2c1 and h2l2 > l2c1:
            r = h2l2 + 0.25 * c1o1
        else:
            api.Result[index] = 0
            return

        k = max(h2c1, l2c1)
        api.Result[index] = 50 * (c2 - c1 + 0.5 * (c2 - o2) + 0.25 * (c1 - o1)) / r * k / api.LimitMoveValue