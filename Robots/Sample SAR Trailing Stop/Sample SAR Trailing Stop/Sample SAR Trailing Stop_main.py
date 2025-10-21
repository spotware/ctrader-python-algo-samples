import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleSARTrailingStop():
    def on_start(self):
        self.parabolicSAR = api.Indicators.ParabolicSAR(api.MinAF, api.MaxAF)
        tradeType = TradeType.Buy if self.parabolicSAR.Result.LastValue < api.Bid else TradeType.Sell
        api.Print(f"Trade type is {tradeType}, Parabolic SAR is {self.parabolicSAR.Result.LastValue}, Bid is {api.Bid}")

        volumeInUnits = api.Symbol.QuantityToVolumeInUnits(api.Quantity);
        api.ExecuteMarketOrder(tradeType, api.SymbolName, volumeInUnits, "PSAR TrailingStops")

    def on_tick(self):
        position = api.Positions.Find("PSAR TrailingStops", api.SymbolName)

        if position is None:
            api.Stop()
        else:
            newStopLoss = self.parabolicSAR.Result.LastValue
            isProtected = position.StopLoss is not None

            if position.TradeType == TradeType.Buy and isProtected:
                if newStopLoss > api.Bid:
                    return
                if newStopLoss - position.StopLoss < api.Symbol.TickSize:
                    return

            if position.TradeType == TradeType.Sell and isProtected:
                if newStopLoss < api.Bid:
                    return
                if position.StopLoss - newStopLoss < api.Symbol.TickSize:
                    return

            api.ModifyPosition(position, newStopLoss, None)