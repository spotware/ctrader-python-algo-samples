using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class RelativeStrengthIndexSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "RelativeStrengthIndexSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Relative Strength Index")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14, Group = "Relative Strength Index", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Down level", DefaultValue = 30, Group = "Relative Strength Index", MinValue = 1, MaxValue = 50)]
    public int DownValue { get; set; }

    [Parameter("Up level", DefaultValue = 70, Group = "Relative Strength Index", MinValue = 50, MaxValue = 100)]
    public int UpValue { get; set; }
}