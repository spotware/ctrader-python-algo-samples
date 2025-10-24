using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class CenterOfGravity : Indicator
{
    [Parameter(DefaultValue = 10, MinValue = 1, MaxValue = 2000)]
    public int Length { get; set; }
    
    [Output("CoG", LineColor = "Red")]
    public IndicatorDataSeries Result { get; set; }

    [Output("Lag", LineColor = "Blue")]
    public IndicatorDataSeries Lag { get; set; }
}
