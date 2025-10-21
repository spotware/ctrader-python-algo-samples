import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

import math

class SampleBreakEven():
    def on_start(self):
        if api.PositionId is None or len(api.PositionId) == 0:
            self.print_error_and_stop("You have to specify \"Position Id\" in cBot Parameters")

        if api.TriggerPips < api.AddPips + 2:
            self.print_error_and_stop("\"Trigger Pips\" must be greater or equal to \"Add Pips\" + 2");

        position = self.find_position_or_stop()
        self.symbolInfo = api.Symbols.GetSymbolInfo(position.SymbolName)

        self.break_even_if_needed()

    def on_tick(self):
        self.break_even_if_needed()

    def break_even_if_needed(self):
        position = self.find_position_or_stop()

        if position.Pips < api.TriggerPips:
            return

        desiredNetProfitInDepositAsset = api.AddPips * self.symbolInfo.PipValue * position.VolumeInUnits
        desiredGrossProfitInDepositAsset = desiredNetProfitInDepositAsset - position.Commissions * 2 - position.Swap
        quoteToDepositRate = self.symbolInfo.PipValue / self.symbolInfo.PipSize
        priceDifference = desiredGrossProfitInDepositAsset / (position.VolumeInUnits * quoteToDepositRate)

        priceAdjustment = self.get_price_adjustment_by_trade_type(position.TradeType, priceDifference)
        breakEvenLevel = position.EntryPrice + priceAdjustment
        roundedBreakEvenLevel = self.round_price(breakEvenLevel, position.TradeType)

        api.ModifyPosition(position, roundedBreakEvenLevel, position.TakeProfit)

        api.Print(f"Stop loss for position PID {position.Id} has been moved to break even.")
        api.Print("Stopping cBot..")
        api.Stop()

    def round_price(self, price, tradeType):
        multiplier = pow(10, self.symbolInfo.Digits)

        if tradeType == TradeType.Buy:
            return math.ceil(price * multiplier) / multiplier

        return math.ceil(price * multiplier) / multiplier

    def get_price_adjustment_by_trade_type(self, tradeType, priceDifference):
        if tradeType == TradeType.Buy:
            return priceDifference;

        return -priceDifference;

    def print_error_and_stop(self, errorMessage):
        api.Print(errorMessage);
        api.Stop();

        raise Exception(errorMessage)

    def find_position_or_stop(self):
        positions = [p for p in api.Positions if f"PID{p.Id}" == api.PositionId or str(p.Id) == api.PositionId]
                
        if len(positions) == 0:
            self.print_error_and_stop(f"Position with Id = {api.PositionId} doesn't exist")

        return positions[0]