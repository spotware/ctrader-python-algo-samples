using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class DataSeriesSample : Indicator
{
    [Parameter()]
    public DataSeries Source { get; set; }
}
