using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
[Cloud("Fast", "Slow", Opacity = 0.2)]
public partial class MACloudSample : Indicator
{
    [Output("Fast", LineColor = "Green", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Fast { get; set; }
        
    [Output("Slow", LineColor = "Red", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Slow { get; set; }
}
