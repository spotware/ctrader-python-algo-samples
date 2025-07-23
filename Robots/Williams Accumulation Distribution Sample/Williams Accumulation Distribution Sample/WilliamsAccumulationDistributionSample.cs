using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class WilliamsAccumulationDistributionSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01, Group = "Trade")]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, Group = "Trade", MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, Group = "Trade", MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "WilliamsAccumulationDistributionSample", Group = "Trade")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Simple Moving Average")]
    public DataSeries SourceMovingAverage { get; set; }

    [Parameter("Periods Moving Average", DefaultValue = 14, Group = "Simple Moving Average", MinValue = 2)]
    public int PeriodsMovingAverage { get; set; }
}