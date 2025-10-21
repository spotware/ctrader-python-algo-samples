import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleGridcBot():
    # This method is called when the cBot starts.
    def on_start(self):
        # Flag to indicate whether there is enough money to open new positions.
        self.enoughMoney = True

        # If there are no grid positions at the start, open the first position.
        if len(self.get_grid_positions()) == 0:
            self.open_position()

    # This method is called on every price tick.
    def on_tick(self):
        # Check if the total net profit of all grid positions exceeds the target profit.
        if sum([p.NetProfit for p in self.get_grid_positions()]) >= api.TargetProfit:
            api.Print("Target profit is reached. Closing all grid positions") # Print a message indicating that the target profit has been reached and all grid positions are closing.
            self.close_grid_positions() # Close all existing positions once the target profit is reached.
            api.Print("All grid positions are closed. Stopping cBot") # Print a message confirming that all grid positions have been closed and the cBot is stopping.
            api.Stop() # Stop the cBot after closing all positions.

        # Check whether there are open grid positions and the funds are sufficient to continue trading.
        if len(self.get_grid_positions()) > 0 and self.enoughMoney:
            # Find the last position in the grid based on the highest number of pips.
            lastGridPosition = sorted(self.get_grid_positions(), key=lambda p: p.Pips)[-1]

            # Calculate the distance in pips from the last grid position.
            distance = self.calculate_distance_in_pips(lastGridPosition)

            # If the price has moved by more than the defined step size, open a new grid position.
            if distance >= api.StepPips:
                self.open_position()

    # Property to get all existing grid positions (buy or sell) for the current symbol.
    def get_grid_positions(self):
        return [p for p in api.Positions if p.SymbolName == api.SymbolName and p.TradeType == api.TradeType]

    # Method to open a new grid position.
    def open_position(self):
        # Execute a market order with the specified trade type, symbol, volume and label.
        result = api.ExecuteMarketOrder(api.TradeType, api.SymbolName, api.Symbol.QuantityToVolumeInUnits(api.VolumeInLots), "Grid")

        # If there is no funds to open the position, set the flag and print a message.
        if result.Error == ErrorCode.NoMoney:
            self.enoughMoney = False
            self.Print("Not enough money to open additional positions")

    # Method to close all grid positions.
    def close_grid_positions(self):
        # Continue closing grid positions until all of them are closed.
        while len(self.get_grid_positions()) > 0:
            for position in self.get_grid_positions():
                api.ClosePosition(position)  # Close each position in the grid.

    # Method to calculate the distance in pips between the last position and the current price.
    def calculate_distance_in_pips(self, position):
        # For buy positions, calculate the distance from the entry price to the current ask price.
        if position.TradeType == TradeType.Buy:
            return (position.EntryPrice - api.Symbol.Ask) / api.Symbol.PipSize
        # For sell positions, calculate the distance from the entry price to the current bid price.
        else:
            return (api.Symbol.Bid - position.EntryPrice) / api.Symbol.PipSize

