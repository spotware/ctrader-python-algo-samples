using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class StandardDeviationSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "StandardDeviationSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Standard Deviation")]
    public DataSeries SourceStandardDeviation { get; set; }

    [Parameter("Periods Standard Deviation", DefaultValue = 20, Group = "Standard Deviation", MinValue = 2)]
    public int PeriodsStandardDeviation { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Standard Deviation")]
    public MovingAverageType MaTypeStandardDeviation { get; set; }

    [Parameter("Source", Group = "Moving Average")]
    public DataSeries SourceMovingAverage { get; set; }

    [Parameter("Periods Moving Average", DefaultValue = 14, Group = "Moving Average", MinValue = 2)]
    public int PeriodsMovingAverage { get; set; }
}