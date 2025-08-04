using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class OrientationSample : Indicator
{
    [Parameter("Orientation", DefaultValue = Orientation.Vertical)]
    public Orientation Orientation { get; set; }
}
