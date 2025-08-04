using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class PenLineCapSample : Indicator
{
    [Parameter("Stroke Start Line Cap", DefaultValue = PenLineCap.Flat)]
    public PenLineCap StrokeStartLineCap { get; set; }

    [Parameter("Stroke End Line Cap", DefaultValue = PenLineCap.Flat)]
    public PenLineCap StrokeEndLineCap { get; set; }

    [Parameter("Stroke Dash Cap", DefaultValue = PenLineCap.Flat)]
    public PenLineCap StrokeDashCap { get; set; }
}
