using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 3, AccessRights = AccessRights.None)]
public partial class SwingIndex : Indicator
{
    [Parameter("Limit Move Value", DefaultValue = 12, MinValue = 1)]
    public int LimitMoveValue { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
