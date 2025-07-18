import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ExponentialMovingAverageSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fastExponentialMovingAverage = api.Indicators.ExponentialMovingAverage(api.SourceFirst, api.PeriodsFirst);
        self.fastExponentialMovingAverage.Result.Line.Color = Color.Blue;
        self.slowExponentialMovingAverage = api.Indicators.ExponentialMovingAverage(api.SourceSecond, api.PeriodsSecond);
        self.slowExponentialMovingAverage.Result.Line.Color = Color.Red;

    def on_bar_closed(self):
        if self.fastExponentialMovingAverage.Result.Last(0) > self.slowExponentialMovingAverage.Result.Last(0) and self.fastExponentialMovingAverage.Result.Last(1) < self.slowExponentialMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label)
        elif self.fastExponentialMovingAverage.Result.Last(0) < self.slowExponentialMovingAverage.Result.Last(0) and self.fastExponentialMovingAverage.Result.Last(1) > self.slowExponentialMovingAverage.Result.Last(1):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)