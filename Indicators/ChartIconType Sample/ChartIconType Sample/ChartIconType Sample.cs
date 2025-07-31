using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class ChartIconTypeSample : Indicator
{
    [Parameter("Icon Type", DefaultValue = ChartIconType.DownArrow)]
    public ChartIconType IconType { get; set; }
}
