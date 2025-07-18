import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class EaseOfMovementSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.easeOfMovement  = api.Indicators.EaseOfMovement(api.Periods, api.MaType)
        self.simpleMovingAverage  = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 9)

    def on_bar_closed(self):
        if self.easeOfMovement.Result.Last(0) > (api.Symbol.TickSize * 0.05):
            if api.Bars.ClosePrices.Last(0) > self.simpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) < self.simpleMovingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
            elif api.Bars.ClosePrices.Last(0) < self.simpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) > self.simpleMovingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        else:
            self.close_positions()

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self):
        for position in self.get_bot_positions():
            api.ClosePosition(position)