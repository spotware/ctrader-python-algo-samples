using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, IsOverlay = false, AccessRights = AccessRights.None)]
public partial class UltimateOscillator : Indicator
{
    [Parameter("Cycle 1", DefaultValue = 7, MinValue = 1)]
    public int Cycle1 { get; set; }

    [Parameter("Cycle 2", DefaultValue = 14, MinValue = 1)]
    public int Cycle2 { get; set; }

    [Parameter("Cycle 3", DefaultValue = 28, MinValue = 1)]
    public int Cycle3 { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
