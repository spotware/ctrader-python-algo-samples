using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class CustomFitnessFunctions : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }
    
    [Parameter("MA Type", Group = "Moving Average")]
    public MovingAverageType MaType { get; set; }

    [Parameter("Source", Group = "Moving Average")]
    public DataSeries SourceSeries { get; set; }

    [Parameter("Slow Periods", Group = "Moving Average", DefaultValue = 10)]
    public int SlowPeriods { get; set; }

    [Parameter("Fast Periods", Group = "Moving Average", DefaultValue = 5)]
    public int FastPeriods { get; set; }
}