using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class AcceleratorOscillator : Indicator
{
    [Parameter("Up", DefaultValue = "Green")]
    public Color UpColor { get; set; }

    [Parameter("Down", DefaultValue = "Red")]
    public Color DownColor { get; set; }

    [Output("Result", PlotType = PlotType.Histogram, IsColorCustomizable = false)]
    public IndicatorDataSeries Result { get; set; }
}
