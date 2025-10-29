using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class PositiveVolumeIndex : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 0, MinValue = 0, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
