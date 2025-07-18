using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class ExponentialMovingAverageSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "ExponentialMovingAverageSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 9, Group = "Exponential Moving Average 1", MinValue = 0)]
    public int PeriodsFirst { get; set; }

    [Parameter("Source", Group = "Exponential Moving Average 1")]
    public DataSeries SourceFirst { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Exponential Moving Average 2", MinValue = 0)]
    public int PeriodsSecond { get; set; }

    [Parameter("Source", Group = "Exponential Moving Average 2")]
    public DataSeries SourceSecond { get; set; }
}