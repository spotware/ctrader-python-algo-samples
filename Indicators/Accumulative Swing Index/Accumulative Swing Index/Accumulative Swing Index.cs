using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class AccumulativeSwingIndex : Indicator
{
    [Parameter("Limit Move Value", DefaultValue = 12, MinValue = 0)]
    public int LimitMoveValue { get; set; }

    [Output("Main", LineColor = "Turquoise")]
    public IndicatorDataSeries Result { get; set; }
}
