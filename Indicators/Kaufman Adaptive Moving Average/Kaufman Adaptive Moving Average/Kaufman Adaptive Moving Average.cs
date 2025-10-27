using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, ScalePrecision = 2, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class KaufmanAdaptiveMovingAverage : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 10, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 2, MinValue = 1)]
    public int FastPeriods { get; set; }

    [Parameter(DefaultValue = 30, MinValue = 1)]
    public int SlowPeriods { get; set; }

    [Output("Main", LineColor = "Turquoise")]
    public IndicatorDataSeries Result { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }
}
