using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None, IsPercentage = true)]
[Levels(20, 80)]
public partial class StochasticOscillator : Indicator
{
    [Parameter("%K Periods", DefaultValue = 9, MinValue = 1)]
    public int KPeriods { get; set; }

    [Parameter("%K Slowing", DefaultValue = 3, MinValue = 1)]
    public int KSlowing { get; set; }

    [Parameter("%D Periods", DefaultValue = 9, MinValue = 0)]
    public int DPeriods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Parameter("Calculation Type", DefaultValue = StochasticCalculationType.LowHigh)]
    public StochasticCalculationType CalculationType { get; set; }

    [Output("%D", LineColor = "Red", LineStyle = LineStyle.Lines)]
    public IndicatorDataSeries PercentD { get; set; }

    [Output("%K", LineColor = "Green")]
    public IndicatorDataSeries PercentK { get; set; }
}
