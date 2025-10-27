using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, IsOverlay = false, AccessRights = AccessRights.None)]
[Levels(20, 80)]
public partial class MoneyFlowIndex : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 2)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
