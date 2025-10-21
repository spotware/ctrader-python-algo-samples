import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleTrendcBot():
    Label = "Sample Trend cBot"

    def on_start(self):
        self.volume_in_units = api.Symbol.QuantityToVolumeInUnits(api.Quantity)
        # Initialise the fast and slow moving averages with the specified periods and type.
        self.fastMa = api.Indicators.MovingAverage(api.SourceSeries, api.FastPeriods, api.MAType)
        self.slowMa = api.Indicators.MovingAverage(api.SourceSeries, api.SlowPeriods, api.MAType)

    def on_tick(self):
        # Find any open buy or sell positions with the specified label and symbol.
        longPosition = api.Positions.Find(self.Label, api.SymbolName, TradeType.Buy)
        shortPosition = api.Positions.Find(self.Label, api.SymbolName, TradeType.Sell)

        # Get the current and previous values of the fast and slow moving averages.
        currentSlowMa = self.slowMa.Result.Last(0) # Current value of the slow moving average.
        currentFastMa = self.fastMa.Result.Last(0) # Current value of the fast moving average.
        previousSlowMa = self.slowMa.Result.Last(1) # Previous value of the slow moving average.
        previousFastMa = self.fastMa.Result.Last(1) # Previous value of the fast moving average.

        # Buy condition - when the slow MA crosses below the fast MA and no long position exists.
        if previousSlowMa > previousFastMa and currentSlowMa <= currentFastMa and longPosition is None:
            if shortPosition is not None: # Close any existing short position.
                api.ClosePosition(shortPosition)
            # Open a new buy order.
            api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.volume_in_units, self.Label)
        # Sell condition - when the slow MA crosses above the fast MA and no short position exists.
        elif previousSlowMa < previousFastMa and currentSlowMa >= currentFastMa and shortPosition is None:
            if longPosition is not None: # Close any existing long position.
                api.ClosePosition(longPosition)
            # Open a new sell order.
            api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.volume_in_units, self.Label)
