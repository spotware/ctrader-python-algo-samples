using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AccessRights = AccessRights.None)]
public partial class Alligator : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter("Jaws Periods", DefaultValue = 13, MinValue = 1, MaxValue = 2000)]
    public int JawsPeriods { get; set; }

    [Parameter("Jaws Shift", DefaultValue = 8, MinValue = 0, MaxValue = 1000)]
    public int JawsShift { get; set; }

    [Parameter("Teeth Periods", DefaultValue = 8, MinValue = 1, MaxValue = 2000)]
    public int TeethPeriods { get; set; }

    [Parameter("Teeth Shift", DefaultValue = 5, MinValue = 0, MaxValue = 1000)]
    public int TeethShift { get; set; }

    [Parameter("Lips Periods", DefaultValue = 5, MinValue = 1, MaxValue = 2000)]
    public int LipsPeriods { get; set; }

    [Parameter("Lips Shift", DefaultValue = 3, MinValue = 0, MaxValue = 1000)]
    public int LipsShift { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple)]
    public MovingAverageType MAType { get; set; }

    [Output("Jaws", LineColor = "Blue")]
    public IndicatorDataSeries Jaws { get; set; }

    [Output("Teeth", LineColor = "Red")]
    public IndicatorDataSeries Teeth { get; set; }

    [Output("Lips", LineColor = "Lime")]
    public IndicatorDataSeries Lips { get; set; }
}
