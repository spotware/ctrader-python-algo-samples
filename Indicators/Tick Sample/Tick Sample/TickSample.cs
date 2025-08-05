using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TickSample : Indicator
{
    [Parameter("Symbol Name", DefaultValue = "EURUSD")]
    public string InputSymbolName { get; set; }
}
