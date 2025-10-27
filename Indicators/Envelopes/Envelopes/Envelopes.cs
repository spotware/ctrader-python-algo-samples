using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class Envelopes : Indicator
{
    [Output("Upper", LineColor = "#B268BCFF")]
    public IndicatorDataSeries Upper { get; set; }

    [Output("Main", LineColor = "#B2B38AB0")]
    public IndicatorDataSeries Main { get; set; }

    [Output("Lower", LineColor = "#B2FF5861")]
    public IndicatorDataSeries Lower { get; set; }

    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Parameter(DefaultValue = 0.2)]
    public double Deviation { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }
}
