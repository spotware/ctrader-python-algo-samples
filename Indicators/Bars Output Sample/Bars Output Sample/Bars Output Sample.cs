using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class BarsOutputSample : Indicator
{
    [Parameter("EMA Periods", DefaultValue = 9)]
    public int EmaPeriods { get; set; }

    [BarOutput("Main")]
    public IndicatorBars Result { get; set; }
}
