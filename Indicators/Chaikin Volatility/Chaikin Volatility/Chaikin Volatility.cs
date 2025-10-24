using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None)]
public partial class ChaikinVolatility : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Rate of Change", DefaultValue = 10, MinValue = 0)]
    public int RateOfChange { get; set; }

    [Parameter("MA Type")]
    public MovingAverageType MAType { get; set; }

    [Output("Main", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }
}
