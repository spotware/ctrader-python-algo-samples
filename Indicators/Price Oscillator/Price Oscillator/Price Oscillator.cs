using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class PriceOscillator : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter("Long Cycle", DefaultValue = 22, MinValue = 1)]
    public int LongCycle { get; set; }

    [Parameter("Short Cycle", DefaultValue = 14, MinValue = 1)]
    public int ShortCycle { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
