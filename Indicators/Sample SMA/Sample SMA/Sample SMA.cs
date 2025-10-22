using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class SampleSMA : Indicator
{
    [Parameter("Source")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14)]
    public int Periods { get; set; }

    [Output("Main", LineColor = "Turquoise")]
    public IndicatorDataSeries Result { get; set; }
}
