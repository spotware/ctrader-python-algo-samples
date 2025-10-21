using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleHotkeyTrading : Robot
{
    [Parameter("Buy", DefaultValue = "Ctrl + Up", Group = "Trading Hotkeys")]
    public string BuyKeys { get; set; }

    [Parameter("Sell", DefaultValue = "Ctrl + Down", Group = "Trading Hotkeys")]
    public string SellKeys { get; set; }

    [Parameter("Close Current Symbol", DefaultValue = "Ctrl + Space", Group = "Trading Hotkeys")]
    public string CloseCurrentSymbolKeys { get; set; }

    [Parameter("Close All", DefaultValue = "Ctrl + Shift + Space", Group = "Trading Hotkeys")]
    public string CloseAllKeys { get; set; }


    [Parameter("Increase small step", DefaultValue = "Ctrl + PageUp", Group = "Volume Hotkeys")]
    public string VolumeIncreaseSmallStepKeys { get; set; }

    [Parameter("Decrease small step", DefaultValue = "Ctrl + PageDown", Group = "Volume Hotkeys")]
    public string VolumeDecreaseSMallStepKeys { get; set; }

    [Parameter("Increase big step", DefaultValue = "Ctrl + Shift + PageUp", Group = "Volume Hotkeys")]
    public string VolumeIncreaseBigStepKeys { get; set; }

    [Parameter("Decrease big step", DefaultValue = "Ctrl + Shift + PageDown", Group = "Volume Hotkeys")]
    public string VolumeDecreaseBigStepKeys { get; set; }


    [Parameter("Default Volume", DefaultValue = 1000, Group = "Volume Steps")]
    public double DefaultVolume { get; set; }

    [Parameter("Small step", DefaultValue = 1000, Group = "Volume Steps")]
    public double VolumeSmallStep { get; set; }

    [Parameter("Big step", DefaultValue = 10000, Group = "Volume Steps")]
    public double VolumeBigStep { get; set; }
}