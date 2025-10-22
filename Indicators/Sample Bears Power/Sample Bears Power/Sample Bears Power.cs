using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(TimeZone = TimeZones.UTC, AccessRights = AccessRights.None)]
public partial class SampleBearsPower : Indicator
{
    [Parameter("Source")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 13, MinValue = 2)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Exponential)]
    public MovingAverageType MAType { get; set; }

    [Output("Result", LineColor = "Orange", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Result { get; set; }
}
