using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None)]
[Levels(-80, -20)]
public partial class WilliamsPctR : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
