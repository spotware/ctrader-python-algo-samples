import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class MomentumOscillatorSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.momentumOscillator = api.Indicators.MomentumOscillator(api.Source, api.PeriodsMomentumOscillator)
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(self.momentumOscillator.Result, api.PeriodsSimpleMovingAverage)

    def on_bar_closed(self):
        if self.momentumOscillator.Result.Last(0) > self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Sell)
            if self.momentumOscillator.Result.Last(1) <= self.simpleMovingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.momentumOscillator.Result.Last(0) < self.simpleMovingAverage.Result.Last(0):
            self.close_positions(TradeType.Buy)
            if self.momentumOscillator.Result.Last(1) >= self.simpleMovingAverage.Result.Last(1):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)