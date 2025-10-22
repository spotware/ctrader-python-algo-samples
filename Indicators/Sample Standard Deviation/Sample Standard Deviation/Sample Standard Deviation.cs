using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(TimeZone = TimeZones.UTC, AccessRights = AccessRights.None)]
public partial class SampleStandardDeviation : Indicator
{
    [Parameter("Source")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 2)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Output("Result", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }
}
