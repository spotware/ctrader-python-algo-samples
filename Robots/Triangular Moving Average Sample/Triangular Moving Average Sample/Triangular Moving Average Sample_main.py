import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class TriangularMovingAverageSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fastTriangularMovingAverage  = api.Indicators.TriangularMovingAverage(api.FastMaSource, api.FastMaPeriod)
        self.slowTriangularMovingAverage  = api.Indicators.TriangularMovingAverage(api.SlowMaSource, api.SlowMaPeriod)

        self.fastTriangularMovingAverage.Result.Line.Color = Color.Blue;
        self.slowTriangularMovingAverage.Result.Line.Color = Color.Red;

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(self.fastTriangularMovingAverage.Result, self.slowTriangularMovingAverage.Result, 0):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif Functions.HasCrossedBelow(self.fastTriangularMovingAverage.Result, self.slowTriangularMovingAverage.Result, 0):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)