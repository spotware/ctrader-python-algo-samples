using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class WebSocketSample : Indicator
{
    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
