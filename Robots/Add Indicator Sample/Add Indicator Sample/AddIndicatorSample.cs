using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None)]
public partial class AddIndicatorSample : Robot
{
    [Parameter("Source", Group = "Moving Average")]
    public DataSeries SourceSeries { get; set; }

    [Parameter("Slow Periods", Group = "Moving Average", DefaultValue = 10)]
    public int SlowPeriods { get; set; }

    [Parameter("Fast Periods", Group = "Moving Average", DefaultValue = 5)]
    public int FastPeriods { get; set; }
}