using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class DeMarker : Indicator
{
    [Parameter("Periods", DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Result", LineColor = "Turquoise")]
    public IndicatorDataSeries Result { get; set; }
}
