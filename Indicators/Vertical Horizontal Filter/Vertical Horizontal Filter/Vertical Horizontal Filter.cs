using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, AccessRights = AccessRights.None)]
public partial class VerticalHorizontalFilter : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }
}
