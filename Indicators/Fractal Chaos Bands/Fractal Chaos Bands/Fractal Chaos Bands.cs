using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class FractalChaosBands : Indicator
{
    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Low", LineColor = "Orange")]
    public IndicatorDataSeries Low { get; set; }

    [Output("High", LineColor = "Green")]
    public IndicatorDataSeries High { get; set; }
}
