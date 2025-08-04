using cAlgo.API;

namespace cAlgo.Indicators;

[Levels(30, 70)]
[Indicator(AccessRights = AccessRights.None, IsOverlay = false)]
public partial class LevelsSample : Indicator
{
    [Parameter(DefaultValue = 9)] 
    public int Periods { get; set; }

    [Output("Main")] 
    public IndicatorDataSeries Result { get; set; }
}