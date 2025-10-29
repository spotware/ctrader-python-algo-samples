using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class RainbowOscillator : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(MinValue = 2, DefaultValue = 9)]
    public int Levels { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
