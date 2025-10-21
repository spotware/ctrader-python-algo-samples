import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

import random

class SampleMartingalecBot():
    def on_start(self):
        # Subscribe to the Positions.Closed event to handle the closing of positions. 
        api.Positions.Closed += self.on_position_closed

        # Execute the first order with the specified initial quantity and a random trade type.
        self.execute_order(api.InitialQuantity, self.get_random_trade_type())

    # Method to execute a market order.
    def execute_order(self, quantity, tradeType):
        # Convert the trade quantity in lots to the volume in units.
        volumeInUnits = api.Symbol.QuantityToVolumeInUnits(quantity)
            
        # Execute a market order with the specified trade type, symbol, volume, label, stop loss and take profit.
        result = api.ExecuteMarketOrder(tradeType, api.SymbolName, volumeInUnits, "Martingale",  api.StopLoss,  api.TakeProfit)

        # If there are no funds to execute the order, stop the cBot.
        if result.Error == ErrorCode.NoMoney:
            api.Stop()

    # This event handler is triggered when a position is closed.
    def on_position_closed(self, args):
        api.Print("Closed")

        position = args.Position

        # Only handle positions labelled as "Martingale" and for the specified symbol.
        if position.Label != "Martingale" or position.SymbolName != api.SymbolName:
            return

        # If the position was profitable, start a new random trade with the specified initial quantity.
        if position.GrossProfit > 0:
            self.execute_order(api.InitialQuantity, self.get_random_trade_type())
        # If the position was a loss, double the trade quantity and continue with the same trade type.
        else:
            self.execute_order(position.Quantity * 2, position.TradeType)

    # Method to randomly choose between the buy or sell trade type.
    def get_random_trade_type(self):
        # Return buy or sell randomly.
        return TradeType.Buy if random.randint(0, 1) == 0 else TradeType.Sell