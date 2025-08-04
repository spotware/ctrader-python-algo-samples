using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class MarketDataSample : Indicator
{
    [Parameter("Use Current Symbol", DefaultValue = true)]
    public bool UseCurrentSymbol { get; set; }

    [Parameter("Other Symbol Name", DefaultValue = "GBPUSD")]
    public string OtherSymbolName { get; set; }

    [Parameter("Use Current TimeFrame", DefaultValue = true)]
    public bool UseCurrentTimeFrame { get; set; }

    [Parameter("Other TimeFrame", DefaultValue = "Daily")]
    public TimeFrame OtherTimeFrame { get; set; }
}
