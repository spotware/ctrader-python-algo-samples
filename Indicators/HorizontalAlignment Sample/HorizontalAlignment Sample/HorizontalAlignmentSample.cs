using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class HorizontalAlignmentSample : Indicator
{
    [Parameter("Horizontal Alignment", DefaultValue = HorizontalAlignment.Center)]
    public HorizontalAlignment HorizontalAlignment { get; set; }
}
