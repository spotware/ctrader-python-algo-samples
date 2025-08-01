using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class KeySample : Indicator
{
    [Parameter(DefaultValue = Key.A)]
    public Key HotKey { get; set; }
}
