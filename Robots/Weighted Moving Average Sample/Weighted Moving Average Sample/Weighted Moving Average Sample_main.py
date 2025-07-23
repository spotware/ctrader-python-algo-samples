import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class WeightedMovingAverageSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fastWeightedMovingAverage  = api.Indicators.WeightedMovingAverage(api.FastMaSource, api.FastMaPeriod)
        self.slowWeightedMovingAverage  = api.Indicators.WeightedMovingAverage(api.SlowMaSource, api.SlowMaPeriod)

        self.fastWeightedMovingAverage.Result.Line.Color = Color.Blue;
        self.slowWeightedMovingAverage.Result.Line.Color = Color.Red;

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(self.fastWeightedMovingAverage.Result, self.slowWeightedMovingAverage.Result, 0):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif Functions.HasCrossedBelow(self.fastWeightedMovingAverage.Result, self.slowWeightedMovingAverage.Result, 0):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)