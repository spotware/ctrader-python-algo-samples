using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class TrueRange : Indicator
{
    [Output("Main", LineColor = "Orange")]
    public IndicatorDataSeries Result { get; set; }
}
