using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class IndicatorDataSeriesSample : Indicator
{
    [Output("Main", LineColor = "Yellow", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Main { get; set; }
}
