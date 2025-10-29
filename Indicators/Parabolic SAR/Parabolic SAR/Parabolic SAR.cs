using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class ParabolicSAR : Indicator
{
    [Parameter("Min AF", DefaultValue = 0.02, MinValue = 0)]
    public double MinAf { get; set; }

    [Parameter("Max AF", DefaultValue = 0.2, MinValue = 0)]
    public double MaxAf { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "Green", LineStyle = LineStyle.Dots, Thickness = 3, PlotType = PlotType.Points)]
    public IndicatorDataSeries Result { get; set; }
}
