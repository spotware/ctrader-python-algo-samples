using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class LinearRegressionForecast : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Output("Forecast", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }

    [Parameter(DefaultValue = 9, MinValue = 0)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }
}
