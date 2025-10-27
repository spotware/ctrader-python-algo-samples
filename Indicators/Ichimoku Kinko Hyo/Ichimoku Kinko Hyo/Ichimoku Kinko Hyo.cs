using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(IsOverlay = true, AutoRescale = false, AccessRights = AccessRights.None)]
public partial class IchimokuKinkoHyo : Indicator
{
    [Parameter("Tenkan Sen Periods", DefaultValue = 9, MinValue = 1)]
    public int TenkanSenPeriods { get; set; }

    [Parameter("Kijun Sen Periods", DefaultValue = 26, MinValue = 1)]
    public int KijunSenPeriods { get; set; }

    [Parameter("Senkou Span B Periods", DefaultValue = 52, MinValue = 1)]
    public int SenkouSpanBPeriods { get; set; }

    [Parameter(DefaultValue = 0, MinValue = -200, MaxValue = 200)]
    public int Shift { get; set; }

    [Output("Tenkan Sen", LineColor = "DodgerBlue")]
    public IndicatorDataSeries TenkanSen { get; set; }

    [Output("Kijun Sen", LineColor = "Crimson")]
    public IndicatorDataSeries KijunSen { get; set; }

    [Output("Chikou Span", LineColor = "MediumSpringGreen")]
    public IndicatorDataSeries ChikouSpan { get; set; }

    [Output("Senkou Span A", LineColor = "SeaGreen")]
    public IndicatorDataSeries SenkouSpanA { get; set; }

    [Output("Senkou Span B", LineColor = "Red")]
    public IndicatorDataSeries SenkouSpanB { get; set; }
}
