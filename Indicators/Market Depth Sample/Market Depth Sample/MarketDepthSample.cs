using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class MarketDepthSample : Indicator
{
    [Output("Bid Entries", LineColor = "Red", PlotType = PlotType.Histogram, Thickness = 5)]
    public IndicatorDataSeries BidResult { get; set; }

    [Output("Ask Entries", LineColor = "Blue", PlotType = PlotType.Histogram, Thickness = 5)]
    public IndicatorDataSeries AskResult { get; set; }
}