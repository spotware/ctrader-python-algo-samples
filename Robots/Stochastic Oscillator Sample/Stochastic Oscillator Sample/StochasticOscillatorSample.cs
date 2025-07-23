using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class StochasticOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "StochasticOscillatorSample")]
    public string Label { get; set; }

    [Parameter("%K Periods", DefaultValue = 9, Group = "Stochastic Oscillator", MinValue = 1)]
    public int KPeriods { get; set; }

    [Parameter("%K Slowing", DefaultValue = 3, Group = "Stochastic Oscillator", MinValue = 1)]
    public int KSlowing { get; set; }

    [Parameter("%D Periods", DefaultValue = 9, Group = "Stochastic Oscillator", MinValue = 0)]
    public int DPeriods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Stochastic Oscillator")]
    public MovingAverageType MaType { get; set; }

    [Parameter("Down level", DefaultValue = 20, Group = "Stochastic Oscillator", MinValue = 1, MaxValue = 50)]
    public int DownValue { get; set; }

    [Parameter("Up level", DefaultValue = 80, Group = "Stochastic Oscillator", MinValue = 50, MaxValue = 100)]
    public int UpValue { get; set; }
}