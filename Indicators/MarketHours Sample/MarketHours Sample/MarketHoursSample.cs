using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class MarketHoursSample : Indicator
{
    [Parameter("Use Current Symbol", DefaultValue = true)]
    public bool UseCurrentSymbol { get; set; }

    [Parameter("Other Symbol Name", DefaultValue = "GBPUSD")]
    public string OtherSymbolName { get; set; }
}
