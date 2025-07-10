import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BollingerBandsMTFCloudSample():
    def initialize(self):
        self.baseBars = api.MarketData.GetBars(api.BaseTimeFrame)
        baseSeries = self.baseBars.GetPrices(api.SourcePriceType)
        self.bollingerBands = api.Indicators.BollingerBands(baseSeries, api.Periods, api.StandardDeviation, api.MaType);
        
    def calculate(self, index):
        baseIndex = self.baseBars.OpenTimes.GetIndexByTime(api.Bars.OpenTimes[index]);
        api.Main[index] = self.bollingerBands.Main[baseIndex];
        api.Top[index] = self.bollingerBands.Top[baseIndex];
        api.Bottom[index] = self.bollingerBands.Bottom[baseIndex];