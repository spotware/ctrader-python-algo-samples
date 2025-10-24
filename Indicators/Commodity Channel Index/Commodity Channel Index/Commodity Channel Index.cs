using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(ScalePrecision = 0, AccessRights = AccessRights.None)]
public partial class CommodityChannelIndex : Indicator
{
    [Parameter(DefaultValue = "Typical")]
    public DataSeries Source { get; set; }
    
    [Parameter(DefaultValue = 20, MinValue = 1)]
    public int Periods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -1000, MaxValue = 1000)]
    public int Shift { get; set; }

    [Output("Main", LineColor = "Green")]
    public IndicatorDataSeries Result { get; set; }
}
