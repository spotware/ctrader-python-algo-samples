using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class BullsPower : Indicator
{
    [Parameter(DefaultValue = 13, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Exponential)]
    public MovingAverageType MAType { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "#8cc44c", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Result { get; set; }
}
