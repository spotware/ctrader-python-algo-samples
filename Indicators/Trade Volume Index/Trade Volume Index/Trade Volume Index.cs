using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class TradeVolumeIndex : Indicator
{
    [Parameter]
    public DataSeries Source { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
