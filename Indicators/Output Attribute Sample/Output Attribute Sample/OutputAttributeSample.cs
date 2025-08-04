using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class OutputAttributeSample : Indicator
{
    [Output("Open", LineColor = "Red", LineStyle = LineStyle.Dots, PlotType = PlotType.Line, Thickness = 2)]
    public IndicatorDataSeries OpenOutput { get; set; }

    [Output("High", LineColor = "Blue", LineStyle = LineStyle.Solid, PlotType = PlotType.Line, Thickness = 2)]
    public IndicatorDataSeries HighOutput { get; set; }

    [Output("Low", LineColor = "Yellow", LineStyle = LineStyle.Lines, PlotType = PlotType.Line, Thickness = 2)]
    public IndicatorDataSeries LowOutput { get; set; }

    [Output("Close", LineColor = "Green", LineStyle = LineStyle.DotsRare, PlotType = PlotType.Line, Thickness = 2)]
    public IndicatorDataSeries CloseOutput { get; set; }
}
