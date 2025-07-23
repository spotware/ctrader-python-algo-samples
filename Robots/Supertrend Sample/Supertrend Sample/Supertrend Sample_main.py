import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SupertrendSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.supertrend = api.Indicators.Supertrend(api.Periods, api.Multiplier)

    def on_bar_closed(self):
        if self.supertrend.UpTrend.Last(0) < api.Bars.LowPrices.Last(0) and self.supertrend.DownTrend.Last(1) > api.Bars.HighPrices.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif self.supertrend.DownTrend.Last(0) > api.Bars.HighPrices.Last(0) and self.supertrend.UpTrend.Last(1) < api.Bars.LowPrices.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)