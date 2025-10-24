using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = false, AccessRights = AccessRights.None)]
public partial class AverageTrueRange : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Output("Main", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }
}
