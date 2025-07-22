import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class RelativeStrengthIndexSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.relativeStrengthIndex = api.Indicators.RelativeStrengthIndex(api.Source, api.Periods)

    def on_bar_closed(self):
        if self.relativeStrengthIndex.Result.Last(0) > api.UpValue and self.relativeStrengthIndex.Result.Last(1) <= api.UpValue:
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.relativeStrengthIndex.Result.Last(0) < api.DownValue and self.relativeStrengthIndex.Result.Last(1) >= api.DownValue:
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)