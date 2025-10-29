using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None)]
public partial class TickVolume : Indicator
{
    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "#2c6dc1", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Result { get; set; }
}
