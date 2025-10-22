using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Cloud(UpperBandLineName, LowerBandLineName)]
[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AccessRights = AccessRights.None)]
public partial class SampleEnvelopesCloud : Indicator
{
    private const string UpperBandLineName = "Upper Band";
    private const string LowerBandLineName = "Lower Band";
    
    [Parameter(DefaultValue = 14)]
    public int Period { get; set; }

    [Parameter(DefaultValue = 0.1)]
    public double Deviation { get; set; }

    [Output(UpperBandLineName, LineColor = "#B268BCFF")]
    public IndicatorDataSeries UpperBand { get; set; }

    [Output(LowerBandLineName, LineColor = "#B2FF5861")]
    public IndicatorDataSeries LowerBand { get; set; }
}
