import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleBreakoutcBot():
    Label = "Sample Breakout cBot"
    # This method is called when the cBot starts.
    def on_start(self):
        # Initialise the Bollinger Bands indicator with the specified parameters.
        self.bollingerBands = api.Indicators.BollingerBands(api.Source, api.Periods, api.Deviations, api.MAType)

    # This method is called on each new bar.
    def on_bar(self):
        # Get the latest values of the top and bottom Bollinger Bands.
        top = self.bollingerBands.Top.Last(1)
        bottom = self.bollingerBands.Bottom.Last(1)

        # Check if the price is within the consolidation range (defined by BandHeightPips).
        if top - bottom <= api.BandHeightPips * api.Symbol.PipSize:
            # Increment for the consolidation counter if the price is within the band.
            self.consolidation += 1
        else:
            # Reset the consolidation counter if the price moves outside the band.
            self.consolidation = 0

        # If the consolidation lasts for the specified number of periods, check for breakout.
        if self.consolidation >= api.ConsolidationPeriods:
            # Convert the trade quantity in lots to the volume in units.
            volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.Quantity)

            # Breakout to the upside: if the ask price is above the top band, place a buy order.
            if api.Ask > top:
                # Execute a buy market order with the specified trade type, symbol, volume, label, stop loss and take profit.
                api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, volumeInUnits, self.Label, api.StopLossInPips, api.TakeProfitInPips)
                self.consolidation = 0  # Reset the consolidation counter after placing a trade.
            # Breakout to the downside: if the bid price is below the bottom band, place a sell order.
            elif api.Bid < bottom:
                # Execute a sell market order with the specified trade type, symbol, volume, label, stop loss and take profit.
                api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, volumeInUnits, self.Label, api.StopLossInPips, api.TakeProfitInPips)
                self.consolidation = 0  # Reset the consolidation counter after placing a trade.