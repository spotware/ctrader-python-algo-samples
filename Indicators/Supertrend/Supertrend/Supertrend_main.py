import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class Supertrend():
    def initialize(self):
        self.trend = api.CreateDataSeries()
        self.upBuffer = api.CreateDataSeries()
        self.downBuffer = api.CreateDataSeries()
        self.averageTrueRange = api.Indicators.AverageTrueRange(api.Periods, MovingAverageType.Simple)
        
    def calculate(self, index):
        self.init_data_series(index)

        median = (api.Bars.HighPrices[index] + api.Bars.LowPrices[index]) / 2
        
        averageTrueRangeValue = self.averageTrueRange.Result[index]

        self.upBuffer[index] = median + api.Multiplier * averageTrueRangeValue
        self.downBuffer[index] = median - api.Multiplier * averageTrueRangeValue

        if index < 1:
            self.trend[index] = 1
            return

        self.calculate_super_trend_logic(index, median, averageTrueRangeValue)
        self.draw_indicator(index)

    def init_data_series(self, index):
        api.UpTrend[index + api.Shift] = float("nan")
        api.DownTrend[index + api.Shift] = float("nan")

    def calculate_super_trend_logic(self, index, median, averageTrueRangeValue):
        if api.Bars.ClosePrices[index] > self.upBuffer[index - 1]:
            self.trend[index] = 1
        elif (api.Bars.ClosePrices[index] < self.downBuffer[index - 1]):
            self.trend[index] = -1
        else:
            match self.trend[index - 1]:
                case 1:
                    self.trend[index] = 1
                case -1:
                    self.trend[index] = -1

        if self.trend[index] < 0 and self.trend[index - 1] > 0:
            self.upBuffer[index] = median + api.Multiplier * averageTrueRangeValue
        elif self.trend[index] < 0 and self.upBuffer[index] > self.upBuffer[index - 1]:
            self.upBuffer[index] = self.upBuffer[index - 1]

        if self.trend[index] > 0 and self.trend[index - 1] < 0:
            self.downBuffer[index] = median - api.Multiplier * averageTrueRangeValue
        elif self.trend[index] > 0 and self.downBuffer[index] < self.downBuffer[index - 1]:
            self.downBuffer[index] = self.downBuffer[index - 1]

    def draw_indicator(self, index):
        match self.trend[index]:
            case 1:
                api.UpTrend[index + api.Shift] = self.downBuffer[index]
            case -1:
                api.DownTrend[index + api.Shift] = self.upBuffer[index]
