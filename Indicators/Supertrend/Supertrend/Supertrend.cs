using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AccessRights = AccessRights.None)]
public partial class Supertrend : Indicator
{
    [Parameter(DefaultValue = 10, MinValue = 1, MaxValue = 2000)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 3.0)]
    public double Multiplier { get; set; }

    [Parameter(DefaultValue = 0, MinValue = 0, MaxValue = 200)]
    public int Shift { get; set; }

    [Output("Up Trend", LineColor = "Green", PlotType = PlotType.Points, Thickness = 2)]
    public IndicatorDataSeries UpTrend { get; set; }

    [Output("Down Trend", LineColor = "Red", PlotType = PlotType.Points, Thickness = 2)]
    public IndicatorDataSeries DownTrend { get; set; }
}
