using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class DonchianChannel : Indicator
{
    [Parameter(DefaultValue = 20, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Top", LineColor = "Red")]
    public IndicatorDataSeries Top { get; set; }

    [Output("Middle")]
    public IndicatorDataSeries Middle { get; set; }

    [Output("Bottom", LineColor = "Blue")]
    public IndicatorDataSeries Bottom { get; set; }
}
