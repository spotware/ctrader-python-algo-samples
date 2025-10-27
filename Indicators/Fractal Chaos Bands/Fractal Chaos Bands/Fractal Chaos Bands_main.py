import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from enum import Enum

class FractalChaosBands():
    def initialize(self):
        self.highFractal = api.CreateDataSeries()
        self.currentPeak = None
 
    def calculate(self, index):
        self.highFractal[index] = (api.Bars.HighPrices[index] + api.Bars.LowPrices[index]) / 3

        self.calculate_high_by(index)
        self.calculate_low_by(index)

        outputIndex = index + api.Shift

        api.High[outputIndex] = self.high3
        api.Low[outputIndex] = self.low3

        self.calculate_fr_by(index)
        self.adjust_fractals_with_fr_by(outputIndex)

    def adjust_fractals_with_fr_by(self, i):
        if self.currentPeak is PeakType.High:
            api.High[i] = self.high3
        else:
            api.High[i] = api.High[i - 1]

        if self.currentPeak is PeakType.Low:
            api.Low[i] = self.low3
        else:
            api.Low[i] = api.Low[i - 1]

    def calculate_fr_by(self, i):
        if self.high3 > self.high1 and self.high3 > self.high2 and self.high3 >= self.high4 and self.high3 >= api.Bars.HighPrices[i]:
            self.currentPeak = PeakType.High
        elif self.low3 < self.low1 and self.low3 < self.low2 and self.low3 <= self.low4 and self.low3 <= api.Bars.LowPrices[i]:
            self.currentPeak = PeakType.Low
        else:
            self.currentPeak = None

    def calculate_low_by(self, i):
        self.low1 = api.Bars.LowPrices[i - 4]
        self.low2 = api.Bars.LowPrices[i - 3]
        self.low3 = api.Bars.LowPrices[i - 2]
        self.low4 = api.Bars.LowPrices[i - 1]

    def calculate_high_by(self, i):
        self.high1 = api.Bars.HighPrices[i - 4]
        self.high2 = api.Bars.HighPrices[i - 3]
        self.high3 = api.Bars.HighPrices[i - 2]
        self.high4 = api.Bars.HighPrices[i - 1]

class PeakType(Enum):
    Low = 1
    High = 2