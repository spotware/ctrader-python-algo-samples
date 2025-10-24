using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class DetrendedPriceOscillator : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 21, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type")]
    public MovingAverageType MAType { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
