using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None, IsPercentage = true)]
public partial class DirectionalMovementSystem : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 1, MaxValue = 10000)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.WilderSmoothing)]
    public MovingAverageType MAType { get; set; }
    
    [Output("ADX", LineColor = "Turquoise")]
    public IndicatorDataSeries ADX { get; set; }

    [Output("DI+", LineColor = "Green")]
    public IndicatorDataSeries DIPlus { get; set; }

    [Output("DI-", LineColor = "Red")]
    public IndicatorDataSeries DIMinus { get; set; }
}
