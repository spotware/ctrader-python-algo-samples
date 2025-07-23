using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SupertrendSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "SupertrendSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 10, Group = "Supertrend", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Multiplier", DefaultValue = 3.0, Group = "Supertrend")]
    public double Multiplier { get; set; }
}