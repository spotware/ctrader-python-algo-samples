using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, AccessRights = AccessRights.None)]
public partial class PriceROC : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 12, MinValue = 1)]
    public int Periods { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
