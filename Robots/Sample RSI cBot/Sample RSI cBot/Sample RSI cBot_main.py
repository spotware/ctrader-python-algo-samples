import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleRSIcBot():
    # This method is called when the cBot starts.
    def on_start(self):
        # Initialise the RSI indicator with the specified source and periods.
        self.rsi = api.Indicators.RelativeStrengthIndex(api.Source, api.Periods)

    # This method is called on every tick. The RSI is recalculated on every tick.
    def on_tick(self):
        # Check if the RSI value is below 30 (oversold condition), signalling a buy opportunity.
        if self.rsi.Result.LastValue < 30:
            self.close_position(TradeType.Sell) # Close any open sell positions.
            self.open_position(TradeType.Buy) # Open a new buy position.
        # Check if the RSI value is above 70 (overbought condition), signalling a sell opportunity.
        elif self.rsi.Result.LastValue > 70:
            self.close_position(TradeType.Buy);  # Close any open buy position.
            self.open_position(TradeType.Sell);  # Open a new sell position.

    # Method to close all positions of the specified trade type (buy or sell). It ensures that opposite positions (e.g., sell positions when a buy is triggered) are closed before new ones are opened.
    def close_position(self, tradeType):
        # Iterate over all positions that match the "SampleRSI" label, specified symbol and trade type.
        for position in api.Positions.FindAll("SampleRSI", api.SymbolName, tradeType):
            api.ClosePosition(position) # Close each found position.

        # Method to open a new position of the specified trade type (buy or sell). It checks for open positions before placing new orders so that duplicate trades are avoided.
    def open_position(self, tradeType):
        # Check if there is an existing position with the same label, symbol and trade type.
        position = api.Positions.Find("SampleRSI", api.SymbolName, tradeType)
            
        # Convert trade quantity in lots to volume in units.
        volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.Quantity)

        # If no existing position is found, execute a new market order.
        if position is None:
            api.ExecuteMarketOrder(tradeType, api.SymbolName, volumeInUnits, "SampleRSI")
