using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class OscillatorMovingAverage : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 13, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Exponential)]
    public MovingAverageType MAType { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "Turquoise", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Histogram { get; set; }
}
