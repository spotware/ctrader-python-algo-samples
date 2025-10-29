using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AccessRights = AccessRights.None)]
public partial class PolynomialRegressionChannels : Indicator
{
    [Parameter(DefaultValue = 3.0, MinValue = 1, MaxValue = 4)]
    public int Degree { get; set; }

    [Parameter(DefaultValue = 120, MinValue = 1, MaxValue = 2000)]
    public int Periods { get; set; }

    [Parameter("Standard Deviation", DefaultValue = 1.62, Step = 0.01)]
    public double StandardDeviation { get; set; }

    [Parameter("Standard Deviation 2", DefaultValue = 2, Step = 0.01)]
    public double StandardDeviation2 { get; set; }

    [Output("PRC", LineColor = "Gray")]
    public IndicatorDataSeries Prc { get; set; }

    [Output("SQH", LineColor = "Red")]
    public IndicatorDataSeries Sqh { get; set; }

    [Output("SQL", LineColor = "Blue")]
    public IndicatorDataSeries Sql { get; set; }

    [Output("SQL2", LineColor = "Blue")]
    public IndicatorDataSeries Sql2 { get; set; }

    [Output("SQH2", LineColor = "Red")]
    public IndicatorDataSeries Sqh2 { get; set; }

    [Parameter(DefaultValue = 0, MinValue = 0, MaxValue = 200)]
    public int Shift { get; set; }
}
