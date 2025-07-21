import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class MacdCrossOverSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.macdCrossOver = api.Indicators.MacdCrossOver(api.Source, api.LongCycle, api.ShortCycle, api.SignalPeriods)

    def on_bar_closed(self):
        if self.macdCrossOver.MACD.Last(0) > self.macdCrossOver.Signal.Last(0) and self.macdCrossOver.MACD.Last(1) <= self.macdCrossOver.Signal.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.macdCrossOver.MACD.Last(0) < self.macdCrossOver.Signal.Last(0) and self.macdCrossOver.MACD.Last(1) >= self.macdCrossOver.Signal.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)