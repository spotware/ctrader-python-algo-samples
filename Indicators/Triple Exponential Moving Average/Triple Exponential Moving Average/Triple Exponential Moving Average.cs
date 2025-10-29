using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, ScalePrecision = 2, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class TripleExponentialMovingAverage : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Output("Main", LineColor = "Turquoise")]
    public IndicatorDataSeries Result { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }
}
