import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class AcceleratorOscillatorSample():
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots);
        self.acceleratorOscillator = api.Indicators.AcceleratorOscillator();

    def on_bar_closed(self):
        for position in self.get_bot_positions():
            if (position.TradeType == TradeType.Buy and self.acceleratorOscillator.Result.Last(0) < self.acceleratorOscillator.Result.Last(1)) or (position.TradeType == TradeType.Sell and self.acceleratorOscillator.Result.Last(0) > self.acceleratorOscillator.Result.Last(1)):
                api.ClosePosition(position);

        if self.acceleratorOscillator.Result.Last(0) > 0 and self.acceleratorOscillator.Result.Last(1) <= 0:
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)
        elif (self.acceleratorOscillator.Result.Last(0) < 0 and self.acceleratorOscillator.Result.Last(1) >= 0):
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, api.Label, api.StopLossInPips, api.TakeProfitInPips)

    def get_bot_positions(self):
        return api.Positions.FindAll(api.Label)