using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class SamplePriceChannels : Indicator
{
    [Parameter(DefaultValue = 20)]
    public int Periods { get; set; }

    [Output("Upper", LineColor = "Pink")]
    public IndicatorDataSeries Upper { get; set; }

    [Output("Lower", LineColor = "Pink")]
    public IndicatorDataSeries Lower { get; set; }

    [Output("Center", LineColor = "Red")]
    public IndicatorDataSeries Center { get; set; }
}
