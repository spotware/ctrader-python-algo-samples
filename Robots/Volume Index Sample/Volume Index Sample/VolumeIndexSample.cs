using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class VolumeIndexSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "VolumeIndexSample")]
    public string Label { get; set; }

    [Parameter("Source for Positive Volume", Group = "Volume Index")]
    public DataSeries PositiveSource { get; set; }

    [Parameter("Source for Negative Volume", Group = "Volume Index")]
    public DataSeries NegativeSource { get; set; }

    [Parameter("Source", Group = "Simple Moving Average")]
    public DataSeries SourceSimpleMovingAverage { get; set; }

    [Parameter("Period", DefaultValue = 20, Group = "Simple Moving Average", MinValue = 1)]
    public int PeriodSimpleMovingAverage { get; set; }
}