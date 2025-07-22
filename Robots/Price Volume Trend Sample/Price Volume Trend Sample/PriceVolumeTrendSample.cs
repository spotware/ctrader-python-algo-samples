using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PriceVolumeTrendSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "PriceVolumeTrendSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Price Volume Trend")]
    public DataSeries SourcePriceVolumeTrend { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Simple Moving Average", MinValue = 0)]
    public int PeriodsSimpleMovingAverage { get; set; }
}