using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None)]
public partial class VolumeOscillator : Indicator
{
    [Parameter("Short Term", DefaultValue = 9, MinValue = 1)]
    public int ShortTerm { get; set; }

    [Parameter("Long Term", DefaultValue = 21, MinValue = 1)]
    public int LongTerm { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
