using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class VolumeOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "VolumeOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Short Term", DefaultValue = 9, Group = "Volume Oscillator", MinValue = 1)]
    public int ShortTerm { get; set; }

    [Parameter("Long Term", DefaultValue = 21, Group = "Volume Oscillator", MinValue = 1)]
    public int LongTerm { get; set; }
}