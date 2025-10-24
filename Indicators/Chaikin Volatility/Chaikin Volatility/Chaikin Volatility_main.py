import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChaikinVolatility():
    def initialize(self):
        self.highMinusLow = api.Indicators.HighMinusLow()
        self.ma = api.Indicators.MovingAverage(self.highMinusLow.Result, api.Periods, api.MAType)
        
    def calculate(self, index):
        maRateOfChangeAgo = self.ma.Result[index - api.RateOfChange]
        maCurrent = self.ma.Result[index]

        api.Result[index] = (maCurrent - maRateOfChangeAgo) / maRateOfChangeAgo * 100