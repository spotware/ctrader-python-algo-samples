import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class RainbowOscillatorSample():
    def on_start(self):
        self.rainbowOscillator = api.Indicators.RainbowOscillator(api.SourceRainbowOscillator, api.LevelsRainbowOscillator, api.MaTypeRainbowOscillator);
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(self.rainbowOscillator.Result, api.PeriodsSimpleMovingAverage);

    def on_bar_closed(self):
        if Functions.HasCrossedAbove(self.rainbowOscillator.Result, self.simpleMovingAverage.Result, 0):
            self.close_positions(TradeType.Buy)
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif Functions.HasCrossedBelow(self.rainbowOscillator.Result, self.simpleMovingAverage.Result, 0):
            self.close_positions(TradeType.Sell)
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)

    def close_positions(self, tradeType):
        for position in self.get_bot_positions():
            if position.TradeType != tradeType:
                continue
            api.ClosePosition(position)