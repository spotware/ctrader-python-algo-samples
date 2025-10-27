using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class MarketFacilitationIndex : Indicator
{
    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "Blue", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Result { get; set; }
}
