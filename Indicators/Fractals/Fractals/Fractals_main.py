import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Fractals():
    def calculate(self, index):
        if index < api.Periods:
            return

        self.draw_up_fractal(index)
        self.draw_down_fractal(index)

    def draw_up_fractal(self, index):
        periods = api.Periods - 1 if api.Periods % 2 == 0 else api.Periods
        middleIndex = index - periods // 2
        middleValue = api.Bars.HighPrices[middleIndex]

        up = True

        for i in range(periods):
            currentIndex = index - i

            if currentIndex == middleIndex or middleValue > api.Bars.HighPrices[currentIndex]:
                continue

            up = False
            break

        fractalIndex = middleIndex + api.Shift
        api.UpFractal[fractalIndex] = middleValue if up else float("nan")

    def draw_down_fractal(self, index):
        periods = api.Periods - 1 if api.Periods % 2 == 0 else api.Periods
        middleIndex = index - periods // 2
        middleValue = api.Bars.LowPrices[middleIndex]

        down = True

        for i in range(periods):
            currentIndex = index - i
            if currentIndex == middleIndex or middleValue < api.Bars.LowPrices[currentIndex]:
                continue

            down = False
            break

        fractalIndex = middleIndex + api.Shift
        api.DownFractal[fractalIndex] = middleValue if down else float("nan")