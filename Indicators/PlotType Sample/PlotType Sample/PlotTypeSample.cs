using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class PlotTypeSample : Indicator
{
    [Output("Discontinuous Line", LineColor = "Red", PlotType = PlotType.DiscontinuousLine)]
    public IndicatorDataSeries DiscontinuousLine { get; set; }

    [Output("Histogram", LineColor = "Green", PlotType = PlotType.Histogram)]
    public IndicatorDataSeries Histogram { get; set; }

    [Output("Line", LineColor = "Blue", PlotType = PlotType.Line)]
    public IndicatorDataSeries Line { get; set; }

    [Output("Points", LineColor = "Yellow", PlotType = PlotType.Points)]
    public IndicatorDataSeries Points { get; set; }
}