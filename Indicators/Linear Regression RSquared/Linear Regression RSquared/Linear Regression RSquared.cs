using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, AccessRights = AccessRights.None)]
public partial class LinearRegressionRSquared : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Output("RSquared", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }

    [Parameter(DefaultValue = 9, MinValue = 1)]
    public int Periods { get; set; }
}
