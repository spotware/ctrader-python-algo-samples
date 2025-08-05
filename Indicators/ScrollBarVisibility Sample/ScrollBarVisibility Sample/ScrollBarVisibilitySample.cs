using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class ScrollBarVisibilitySample : Indicator
{
    [Parameter("Horizontal Scroll Bar Visibility", DefaultValue = ScrollBarVisibility.Auto)]
    public ScrollBarVisibility HorizontalScrollBarVisibility { get; set; }

    [Parameter("Vertical Scroll Bar Visibility", DefaultValue = ScrollBarVisibility.Visible)]
    public ScrollBarVisibility VerticalScrollBarVisibility { get; set; }
}
