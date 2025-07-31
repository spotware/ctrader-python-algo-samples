using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class ControlAlignmentSample : Indicator
{
    [Parameter("Horizontal Alignment", DefaultValue = HorizontalAlignment.Center)]
    public HorizontalAlignment HorizontalAlignment { get; set; }

    [Parameter("Vertical Alignment", DefaultValue = VerticalAlignment.Center)]
    public VerticalAlignment VerticalAlignment { get; set; }
}
