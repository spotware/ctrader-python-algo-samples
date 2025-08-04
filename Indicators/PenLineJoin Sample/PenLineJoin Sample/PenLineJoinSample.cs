using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class PenLineJoinSample : Indicator
{
    [Parameter("Stroke Line Join", DefaultValue = PenLineJoin.Miter)]
    public PenLineJoin StrokeLineJoin { get; set; }
}
