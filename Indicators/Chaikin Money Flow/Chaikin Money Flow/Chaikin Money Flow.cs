using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class ChaikinMoneyFlow : Indicator
{
    [Parameter(DefaultValue = 14, MinValue = 1)]
    public int Periods { get; set; }

    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }
}
