using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class WrapPanelSample : Indicator
{
    [Parameter("Panel Orientation", DefaultValue = Orientation.Vertical)]
    public Orientation PanelOrientation { get; set; }
}
