using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class TypicalPrice : Indicator
{
    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
