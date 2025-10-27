using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 3, AccessRights = AccessRights.None)]
public partial class HistoricalVolatility : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 20, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Bar History", DefaultValue = 252)]
    public int BarHistory { get; set; }

    [Output("Main", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }
}
