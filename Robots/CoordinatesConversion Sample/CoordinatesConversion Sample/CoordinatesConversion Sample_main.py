import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class CoordinatesConversionSample():
    def on_start(self):
        # Assigning a custom event handler to the Chart.MouseUp event
        api.Chart.MouseUp += self.chart_mouse_up

    def chart_mouse_up(self, args):
        # Using the Chart.YToYValue() method to convert coordinates into a symbol price
        desiredPrice = api.Chart.YToYValue(args.MouseY);
            
        # Using a ternary operator to determine the trade type
        # A buy order is placed if the mouse is under the current symbol bid
        # A sell order is placed if the mouse is above the current symbol bid
        desiredTradeType = TradeType.Sell if desiredPrice > api.Symbol.Bid else TradeType.Buy;
            
        api.PlaceLimitOrder(desiredTradeType, api.SymbolName, 10000, desiredPrice);