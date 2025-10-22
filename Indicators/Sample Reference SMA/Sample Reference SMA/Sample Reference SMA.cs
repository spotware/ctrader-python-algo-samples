using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class SampleReferenceSMA : Indicator
{
    [Parameter("Source")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14)]
    public int SmaPeriod { get; set; }

    [Output("Referenced SMA Output")]
    public IndicatorDataSeries RefSMA { get; set; }
}
