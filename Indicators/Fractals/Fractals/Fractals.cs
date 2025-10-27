using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AccessRights = AccessRights.None)]
public partial class Fractals : Indicator
{
    [Parameter(DefaultValue = 5, MinValue = 5, MaxValue = 2000)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = 0, MaxValue = 200)]
    public int Shift { get; set; }

    [Output("Up Fractal", LineColor = "Red", PlotType = PlotType.Points, Thickness = 2)]
    public IndicatorDataSeries UpFractal { get; set; }

    [Output("Down Fractal", LineColor = "Blue", PlotType = PlotType.Points, Thickness = 2)]
    public IndicatorDataSeries DownFractal { get; set; }
}
