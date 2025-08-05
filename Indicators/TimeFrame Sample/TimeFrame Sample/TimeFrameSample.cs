using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TimeFrameSample : Indicator
{
    [Parameter("Time Frame", DefaultValue = "Daily")]
    public TimeFrame UserSelectedTimeFrame { get; set; }
}
