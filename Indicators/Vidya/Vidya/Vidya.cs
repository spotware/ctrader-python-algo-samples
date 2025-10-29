using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class Vidya : Indicator
{
    [Parameter]
    public DataSeries Price { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Sigma", DefaultValue = 0.65, MinValue = 0.1, MaxValue = 0.95)]
    public double Sigma { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
