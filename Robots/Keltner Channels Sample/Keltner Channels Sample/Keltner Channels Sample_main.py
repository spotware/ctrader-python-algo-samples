import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class KeltnerChannelsSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.keltnerChannels = api.Indicators.KeltnerChannels(api.MaPeriod, api.MaType, api.AtrPeriod, api.AtrMaType, api.BandDistance)

    def on_bar_closed(self):
        if api.Bars.LowPrices.Last(0) <= self.keltnerChannels.Bottom.Last(0) and api.Bars.LowPrices.Last(1) > self.keltnerChannels.Bottom.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label)
        elif api.Bars.HighPrices.Last(0) >= self.keltnerChannels.Top.Last(0) and api.Bars.HighPrices.Last(1) < self.keltnerChannels.Top.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)