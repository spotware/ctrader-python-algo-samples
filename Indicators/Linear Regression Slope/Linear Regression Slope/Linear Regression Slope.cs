using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class LinearRegressionSlope : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 9, MinValue = 1)]
    public int Periods { get; set; }

    [Output("Slope", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
