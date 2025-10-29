using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 2, IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class WeightedClose : Indicator
{
    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
