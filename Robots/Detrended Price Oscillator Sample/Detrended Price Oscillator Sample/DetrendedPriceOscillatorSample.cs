using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class DetrendedPriceOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "DetrendedPriceOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 21, Group = "Detrended Price Oscillator", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", Group = "Detrended Price Oscillator")]
    public MovingAverageType MaType { get; set; }
}