using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class RelativeVigorIndex : Indicator
{
    [Parameter("Periods", DefaultValue = 10, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Result", LineColor = "Blue")]
    public IndicatorDataSeries Result { get; set; }

    [Output("Signal", LineColor = "Red", LineStyle = LineStyle.Lines)]
    public IndicatorDataSeries Signal { get; set; }
}
