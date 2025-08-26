using System;
using cAlgo.API;

namespace cAlgo.Indicators;

// You can set IsOverlay to true if you want to show the bars output
// in main chart panel.
[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class BarsOutputSample : Indicator
{
    [Parameter("EMA Periods", DefaultValue = 9)]
    public int EmaPeriods { get; set; }

    [BarOutput("Main")]
    public IndicatorBars Result { get; set; }
}
