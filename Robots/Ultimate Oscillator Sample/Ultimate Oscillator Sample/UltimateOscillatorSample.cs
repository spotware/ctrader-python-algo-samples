using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class UltimateOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "UltimateOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Cycle 1", DefaultValue = 7, Group = "Ultimate Oscillator", MinValue = 1)]
    public int Cycle1 { get; set; }

    [Parameter("Cycle 2", DefaultValue = 14, Group = "Ultimate Oscillator", MinValue = 1)]
    public int Cycle2 { get; set; }

    [Parameter("Cycle 3", DefaultValue = 28, Group = "Ultimate Oscillator", MinValue = 1)]
    public int Cycle3 { get; set; }

    [Parameter("Down level", DefaultValue = 30, Group = "Stochastic Oscillator", MinValue = 1, MaxValue = 50)]
    public int DownValue { get; set; }

    [Parameter("Up level", DefaultValue = 70, Group = "Stochastic Oscillator", MinValue = 50, MaxValue = 100)]
    public int UpValue { get; set; }
}