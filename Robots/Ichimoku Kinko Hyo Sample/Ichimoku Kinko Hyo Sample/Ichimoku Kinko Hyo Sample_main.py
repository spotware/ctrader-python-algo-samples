import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class IchimokuKinkoHyoSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.ichimokuKinkoHyo = api.Indicators.IchimokuKinkoHyo(api.TenkanSenPeriods, api.KijunSenPeriods, api.SenkouSpanBPeriods)

    def on_bar_closed(self):
        if api.Bars.ClosePrices.Last(0) > self.ichimokuKinkoHyo.SenkouSpanB.Last(0):
            self.close_positions(TradeType.Sell)
            if self.ichimokuKinkoHyo.TenkanSen.Last(0) > self.ichimokuKinkoHyo.KijunSen.Last(0) and self.ichimokuKinkoHyo.TenkanSen.Last(1) <= self.ichimokuKinkoHyo.KijunSen.Last(1):
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif api.Bars.ClosePrices.Last(0) < self.ichimokuKinkoHyo.SenkouSpanA.Last(0):
            self.close_positions(TradeType.Buy)
            if self.ichimokuKinkoHyo.TenkanSen.Last(0) < self.ichimokuKinkoHyo.KijunSen.Last(0) and self.ichimokuKinkoHyo.TenkanSen.Last(1) >= self.ichimokuKinkoHyo.KijunSen.Last(1):
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)