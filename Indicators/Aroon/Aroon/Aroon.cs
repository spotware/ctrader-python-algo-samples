using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None, IsPercentage = true)]
public partial class Aroon : Indicator
{
    [Parameter(DefaultValue = 25, MinValue = 2)]
    public int Periods { get; set; }

    [Output("Up", LineColor = "Turquoise")]
    public IndicatorDataSeries Up { get; set; }

    [Output("Down", LineColor = "Red")]
    public IndicatorDataSeries Down { get; set; }
}
