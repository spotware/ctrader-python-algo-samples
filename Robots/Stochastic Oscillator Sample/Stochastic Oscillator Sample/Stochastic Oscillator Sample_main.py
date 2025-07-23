import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class StochasticOscillatorSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.stochasticOscillator = api.Indicators.StochasticOscillator(api.KPeriods, api.KSlowing, api.DPeriods, api.MaType)

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(self.stochasticOscillator.PercentK, self.stochasticOscillator.PercentD, 0) and self.stochasticOscillator.PercentK.Last(1) <= api.DownValue:
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif Functions.HasCrossedBelow(self.stochasticOscillator.PercentK, self.stochasticOscillator.PercentD, 0) and self.stochasticOscillator.PercentK.Last(1) >= api.UpValue:
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)