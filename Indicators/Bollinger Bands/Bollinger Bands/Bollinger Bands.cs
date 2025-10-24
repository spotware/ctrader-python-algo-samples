using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class BollingerBands : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 20, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Standard Dev", DefaultValue = 2.0, MinValue = 0.0001, MaxValue = 10)]
    public double StandardDeviations { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Main { get; set; }

    [Output("Top")]
    public IndicatorDataSeries Top { get; set; }

    [Output("Bottom")]
    public IndicatorDataSeries Bottom { get; set; }
}
