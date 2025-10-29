using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class VariableIndexDynamicAverage : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int CMOPeriods { get; set; }

    [Parameter(DefaultValue = 2, MinValue = 1)]
    public double SmoothPeriods { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
