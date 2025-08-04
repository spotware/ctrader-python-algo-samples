using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class ModifierKeysSample : Indicator
{
    [Parameter(DefaultValue = Key.R)]
    public Key HotKey { get; set; }

    [Parameter(DefaultValue = ModifierKeys.Control)]
    public ModifierKeys HotKeyModifier { get; set; }
}
