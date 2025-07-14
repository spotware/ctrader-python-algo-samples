using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class CommodityChannelIndexSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "CommodityChannelIndexSample")]
    public string Label { get; set; }

    [Parameter(DefaultValue = 20, Group = "Commodity Channel Index", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Down level", DefaultValue = -100, Group = "Commodity Channel Index")]
    public int DownValue { get; set; }

    [Parameter("Up level", DefaultValue = 100, Group = "Commodity Channel Index")]
    public int UpValue { get; set; }
}