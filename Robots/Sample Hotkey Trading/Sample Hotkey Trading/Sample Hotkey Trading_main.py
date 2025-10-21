import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import Action

class SampleHotkeyTrading():
    def on_start(self):
        self.current_volume = api.DefaultVolume

        self.update_volume_label()

        api.Chart.AddHotkey(Action(self.buy), api.BuyKeys)
        api.Chart.AddHotkey(Action(self.sell), api.SellKeys)
        api.Chart.AddHotkey(Action(self.close_position_for_current_symbol), api.CloseCurrentSymbolKeys)
        api.Chart.AddHotkey(Action(self.close_all_positions), api.CloseAllKeys)

        api.Chart.AddHotkey(Action[ChartKeyboardEventArgs](lambda _: self.increase_volume(api.VolumeSmallStep)), api.VolumeIncreaseSmallStepKeys)
        api.Chart.AddHotkey(Action[ChartKeyboardEventArgs](lambda _: self.increase_volume(api.VolumeBigStep)), api.VolumeIncreaseBigStepKeys)
        api.Chart.AddHotkey(Action[ChartKeyboardEventArgs](lambda _: self.decrease_volume(api.VolumeSmallStep)), api.VolumeDecreaseSMallStepKeys)
        api.Chart.AddHotkey(Action[ChartKeyboardEventArgs](lambda _: self.decrease_volume(api.VolumeBigStep)), api.VolumeDecreaseBigStepKeys)

    def buy(self):
        api.Print("Hotkey triggered: Buy")
        api.ExecuteMarketOrder(TradeType.Buy, api.SymbolName, self.current_volume)

    def sell(self):
        api.Print("Hotkey triggered: Sell")
        api.ExecuteMarketOrder(TradeType.Sell, api.SymbolName, self.current_volume)

    def close_position_for_current_symbol(self):
        api.Print("Hotkey triggered: Close current symbol positions")

        for position in api.Positions:
            if position.SymbolName == api.SymbolName:
                api.ClosePositionAsync(position)

    def close_all_positions(self):
        api.Print("Hotkey triggered: Close all position")

        for position in api.Positions:
                api.ClosePositionAsync(position)

    def increase_volume(self, volumeDelta):
        self.current_volume = min(self.current_volume + volumeDelta, api.Symbol.VolumeInUnitsMax)
        self.update_volume_label()

    def decrease_volume(self, volumeDelta):
        self.current_volume = max(self.current_volume - volumeDelta, api.Symbol.VolumeInUnitsMin)
        self.update_volume_label()

    def update_volume_label(self):
        text = f"Volume {self.current_volume}"
        api.Chart.DrawStaticText("volume", text, VerticalAlignment.Top, HorizontalAlignment.Left, api.Chart.ColorSettings.ForegroundColor)