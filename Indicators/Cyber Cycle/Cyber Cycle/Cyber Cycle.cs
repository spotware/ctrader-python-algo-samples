using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class CyberCycle : Indicator
{
    [Parameter(DefaultValue = 0.07, MinValue = 0.01, MaxValue = 100, Step = 0.01)]
    public double Alpha { get; set; }

    [Output("Cyber Cycle", LineColor = "Red")]
    public IndicatorDataSeries Cycle { get; set; }

    [Output("Trigger", LineColor = "Blue")]
    public IndicatorDataSeries Trigger { get; set; }
}
