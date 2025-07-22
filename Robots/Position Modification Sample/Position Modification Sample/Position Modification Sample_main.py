import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionModificationSample():
    def on_start(self):
        positions = []

        if len(api.PositionComment) > 0 and len(api.PositionLabel) > 0:
            positions = [position for position in api.Positions.FindAll(api.PositionLabel) if position.Comment == api.PositionComment]
        elif len(api.PositionComment) > 0:
            positions = [position for position in api.Positions if position.Comment == api.PositionComment]
        elif len(api.PositionLabel) > 0:
            positions = [position for position in api.Positions.FindAll(api.PositionLabel)]

        if len(positions) == 0:
            api.Print("Couldn't find matching postions, please check the comment and label")
        else:
            for position in positions:
                self.modify_position(position)

        api.Stop()

    def modify_position(self, position):
        positionSymbol = api.Symbols.GetSymbol(position.SymbolName)

        stopLossInPrice = position.StopLoss

        if api.StopLossInPips > 0:
            stopLossInPipsPrice = api.StopLossInPips * positionSymbol.PipSize
            stopLossInPrice = position.EntryPrice - stopLossInPipsPrice if position.TradeType == TradeType.Buy else position.EntryPrice + stopLossInPipsPrice

        takeProfitInPrice = position.TakeProfit

        if api.TakeProfitInPips > 0:
            takeProfitInPipsPrice = api.TakeProfitInPips * positionSymbol.PipSize
            takeProfitInPrice = position.EntryPrice + takeProfitInPipsPrice if position.TradeType == TradeType.Buy else position.EntryPrice - takeProfitInPipsPrice

        api.ModifyPosition(position, stopLossInPrice, takeProfitInPrice, api.HasTrailingStop, api.StopLossTriggerMethod)

        if api.VolumeInLots > 0:
            volumeInUnits = positionSymbol.QuantityToVolumeInUnits(api.VolumeInLots)
            api.ModifyPosition(position, volumeInUnits)