using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, TimeZone = TimeZones.UTC, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class SampleAlligator : Indicator
{
    [Parameter("Periods", Group = "Jaws", DefaultValue = 13)]
    public int JawsPeriods { get; set; }

    [Parameter("Shift", Group = "Jaws", DefaultValue = 8)]
    public int JawsShift { get; set; }

    [Parameter("Periods", Group = "Teeth", DefaultValue = 8)]
    public int TeethPeriods { get; set; }

    [Parameter("Shift", Group = "Teeth", DefaultValue = 5)]
    public int TeethShift { get; set; }

    [Parameter("Periods", Group = "Lips", DefaultValue = 5)]
    public int LipsPeriods { get; set; }

    [Parameter("Shift", Group = "Lips", DefaultValue = 3)]
    public int LipsShift { get; set; }

    [Output("Jaws", LineColor = "Blue")]
    public IndicatorDataSeries Jaws { get; set; }

    [Output("Teeth", LineColor = "Red")]
    public IndicatorDataSeries Teeth { get; set; }

    [Output("Lips", LineColor = "Lime")]
    public IndicatorDataSeries Lips { get; set; }
}
