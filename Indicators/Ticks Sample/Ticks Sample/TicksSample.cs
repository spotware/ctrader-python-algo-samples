using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TicksSample : Indicator
{
    [Parameter("Symbol Name", DefaultValue = "EURUSD")]
    public string InputSymbolName { get; set; }
}
