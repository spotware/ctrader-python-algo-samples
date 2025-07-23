import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class VolumeOscillatorSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.volumeOscillator = api.Indicators.VolumeOscillator(api.ShortTerm, api.LongTerm)
        self.volumeOscillatorSimpleMovingAverage = api.Indicators.SimpleMovingAverage(self.volumeOscillator.Result, 14)
        self.priceSimpleMovingAverage = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 14)

    def on_bar_closed(self):
        if self.volumeOscillator.Result.Last(0) < self.volumeOscillatorSimpleMovingAverage.Result.Last(0):
            return

        if api.Bars.ClosePrices.Last(0) > self.priceSimpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) <= self.priceSimpleMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.priceSimpleMovingAverage.Result.Last(0) and api.Bars.ClosePrices.Last(1) >= self.priceSimpleMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)