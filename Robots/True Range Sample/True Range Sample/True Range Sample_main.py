import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class TrueRangeSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.trueRange = api.Indicators.TrueRange()

    def on_bar_closed(self):
        if api.Bars.ClosePrices.Last(0) > api.Bars.OpenPrices.Last(0) and api.Bars.ClosePrices.Last(1) < api.Bars.OpenPrices.Last(1):
            self.close_positions(TradeType.Sell)
            self.execute_order(TradeType.Buy)
        elif api.Bars.ClosePrices.Last(0) < api.Bars.OpenPrices.Last(0) and api.Bars.ClosePrices.Last(1) > api.Bars.OpenPrices.Last(1):
            self.close_positions(TradeType.Buy)
            self.execute_order(TradeType.Sell)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)

    def execute_order(self, tradeType):
        trueRangeInPips = self.trueRange.Result.Last(1) * (api.Symbol.TickSize / api.Symbol.PipSize * pow(10, api.Symbol.Digits))
        stopLossInPips = trueRangeInPips * 2;
        takeProfitInPips = stopLossInPips * 2;
        api.ExecuteMarketOrder(tradeType, api.SymbolName, self.volumeInUnits, api.Label, stopLossInPips, takeProfitInPips)