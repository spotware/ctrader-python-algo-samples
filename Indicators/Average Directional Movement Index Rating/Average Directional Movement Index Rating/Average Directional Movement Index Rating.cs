using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = false, AccessRights = AccessRights.None, IsPercentage = true)]
public partial class AverageDirectionalMovementIndexRating : Indicator
{
    [Parameter(DefaultValue = 14)]
    public int Periods { get; set; }
    
    [Parameter("MA Type", DefaultValue = MovingAverageType.WilderSmoothing)]
    public MovingAverageType MAType { get; set; }
    
    [Output("ADX", LineColor = "Turquoise")]
    public IndicatorDataSeries ADX { get; set; }

    [Output("ADXR", LineColor = "Gold")]
    public IndicatorDataSeries ADXR { get; set; }

    [Output("DI-", LineColor = "Red")]
    public IndicatorDataSeries DIMinus { get; set; }

    [Output("DI+", LineColor = "Green")]
    public IndicatorDataSeries DIPlus { get; set; }
}
