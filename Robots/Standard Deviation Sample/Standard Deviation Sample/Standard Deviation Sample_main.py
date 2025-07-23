import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class StandardDeviationSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.standardDeviation = api.Indicators.StandardDeviation(api.SourceStandardDeviation, api.PeriodsStandardDeviation, api.MaTypeStandardDeviation);
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.SourceMovingAverage, api.PeriodsMovingAverage);

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(api.Bars.ClosePrices, self.simpleMovingAverage.Result, 0):
            self.close_positions(TradeType.Sell)
            self.execute_order(TradeType.Buy)
        elif Functions.HasCrossedBelow(api.Bars.ClosePrices, self.simpleMovingAverage.Result, 0):
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
        standardDeviationInPips = self.standardDeviation.Result.Last(1) * (api.Symbol.TickSize / api.Symbol.PipSize * pow(10, api.Symbol.Digits))
        stopLossInPips = standardDeviationInPips * 2;
        takeProfitInPips = stopLossInPips * 2;
        api.ExecuteMarketOrder(tradeType, api.SymbolName, self.volumeInUnits, api.Label, stopLossInPips, takeProfitInPips)