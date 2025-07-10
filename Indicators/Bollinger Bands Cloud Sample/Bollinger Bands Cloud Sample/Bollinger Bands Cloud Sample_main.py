import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BollingerBandsCloudSample():
    def initialize(self):
        self.bollingerBands = api.Indicators.BollingerBands(api.Bars.ClosePrices, 20, 2, MovingAverageType.Simple);
        
    def calculate(self, index):
        api.Main[index] = self.bollingerBands.Main[index];
        api.Top[index] = self.bollingerBands.Top[index];
        api.Bottom[index] = self.bollingerBands.Bottom[index];