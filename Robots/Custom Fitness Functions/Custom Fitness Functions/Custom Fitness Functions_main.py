import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class CustomFitnessFunctions():
    LABEL = "CustomFitnessFunctions";
    def on_start(self):
        self.volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots)
        self.fastMa = api.Indicators.MovingAverage(api.SourceSeries, api.FastPeriods, api.MaType)
        self.slowMa = api.Indicators.MovingAverage(api.SourceSeries, api.SlowPeriods, api.MaType)
    
    def on_tick(self):
        longPosition = api.Positions.Find(self.LABEL, api.SymbolName, TradeType.Buy)
        shortPosition = api.Positions.Find(self.LABEL, api.SymbolName, TradeType.Sell)

        currentSlowMa = self.slowMa.Result.Last(0);
        currentFastMa = self.fastMa.Result.Last(0);
        previousSlowMa = self.slowMa.Result.Last(1);
        previousFastMa = self.fastMa.Result.Last(1);

        if previousSlowMa > previousFastMa and currentSlowMa <= currentFastMa and longPosition is None:
            if shortPosition is not None:
                api.ClosePosition(shortPosition)

            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volumeInUnits, self.LABEL)
        elif previousSlowMa < previousFastMa and currentSlowMa >= currentFastMa and shortPosition is None:
            if longPosition is not None:
                api.ClosePosition(longPosition)

            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volumeInUnits, self.LABEL)

    def get_fitness(self, args):
        if args.TotalTrades > 20 and args.MaxEquityDrawdownPercentages < 50:
            return pow(args.WinningTrades + 1, 2) / (args.LosingTrades + 1)
        else:
            return -1