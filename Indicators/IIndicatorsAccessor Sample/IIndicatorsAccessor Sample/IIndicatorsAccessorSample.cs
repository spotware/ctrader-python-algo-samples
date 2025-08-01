using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class IIndicatorsAccessorSample : Indicator
{
    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
