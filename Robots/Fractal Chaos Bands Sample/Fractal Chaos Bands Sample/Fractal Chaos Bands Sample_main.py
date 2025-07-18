import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class FractalChaosBandsSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fractalChaosBands  = api.Indicators.FractalChaosBands()

    def on_bar_closed(self):
        if api.Bars.ClosePrices.Last(0) > self.fractalChaosBands.High.Last(0) and api.Bars.ClosePrices.Last(1) <= self.fractalChaosBands.High.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.fractalChaosBands.Low.Last(0) and api.Bars.ClosePrices.Last(1) >= self.fractalChaosBands.Low.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)