using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class MacdOscillatorMovingAverage : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter("Long Cycle", DefaultValue = 26, MinValue = 1)]
    public int LongCycle { get; set; }

    [Parameter("Short Cycle", DefaultValue = 12, MinValue = 1)]
    public int ShortCycle { get; set; }

    [Parameter("Signal Periods", DefaultValue = 9, MinValue = 1)]
    public int SignalPeriods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Exponential)]
    public MovingAverageType MAType { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "Turquoise", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Histogram { get; set; }
}
