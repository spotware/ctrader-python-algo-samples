import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class MovingAverageSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fastMa = api.Indicators.MovingAverage(api.FastMaSource, api.FastMaPeriod, api.FastMaType);
        self.slowMa = api.Indicators.MovingAverage(api.SlowMaSource, api.SlowMaPeriod, api.SlowMaType);

        self.fastMa.Result.Line.Color = Color.Blue;
        self.slowMa.Result.Line.Color = Color.Red;

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(self.fastMa.Result, self.slowMa.Result, 0):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif Functions.HasCrossedBelow(self.fastMa.Result, self.slowMa.Result, 0):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)