using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class MoneyFlowIndexSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "MoneyFlowIndexSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 14, Group = "Money Flow Index", MinValue = 2)]
    public int Periods { get; set; }

    [Parameter("Level Up", DefaultValue = 80, Group = "Money Flow Index", MinValue = 50, MaxValue = 100)]
    public int LevelUp { get; set; }

    [Parameter("Level Down", DefaultValue = 20, Group = "Money Flow Index", MinValue = 0, MaxValue = 50)]
    public int LevelDown { get; set; }
}