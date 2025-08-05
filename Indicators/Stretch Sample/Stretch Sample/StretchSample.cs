using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class StretchSample : Indicator
{
    [Parameter("Stretch", DefaultValue = Stretch.Uniform)]
    public Stretch Stretch { get; set; }
}
