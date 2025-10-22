using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(TimeZone = TimeZones.UTC, AccessRights = AccessRights.None)]
public partial class SampleDeMarker : Indicator
{
    [Parameter(DefaultValue = 14)]
    public int Periods { get; set; }

    [Output("DMark", LineColor = "Turquoise")]
    public IndicatorDataSeries DMark { get; set; }
}
