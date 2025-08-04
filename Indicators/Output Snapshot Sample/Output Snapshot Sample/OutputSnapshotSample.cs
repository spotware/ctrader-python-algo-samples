using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class OutputSnapshotSample : Indicator
{
    [Parameter("Tolerance (Pips)", DefaultValue = 8)]
    public double ToleranceInPips { get; set; }

    [Output("Main", LineColor = "Yellow", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Main { get; set; }
}
