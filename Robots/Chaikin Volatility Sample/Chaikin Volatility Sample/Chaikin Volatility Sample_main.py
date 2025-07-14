import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ChaikinVolatilitySample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.chaikinVolatility = api.Indicators.ChaikinVolatility(api.ChaikinPeriods, api.RateOfChange, api.MaTypeChaikin)
        self.movingAverage = api.Indicators.MovingAverage(api.Bars.ClosePrices, api.SmaPeriods, api.MaType)

    def on_bar_closed(self):
        if self.chaikinVolatility.Result.Last(0) > 0:
            if api.Bars.ClosePrices.Last(0) > self.movingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) < self.movingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
            elif api.Bars.ClosePrices.Last(0) < self.movingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) > self.movingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        else:
            self.close_positions()

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self):
        for position in self.get_bot_positions():
            api.ClosePosition(position)