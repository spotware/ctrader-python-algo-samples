using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class PositionCurrentPriceSample : Indicator
{
    [Output("Result", LineColor = "Orange", PlotType = PlotType.Line)]
    public IndicatorDataSeries Result { get; set; }
}
