using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PositionBarsPassedSample : Robot
{
    [Parameter("Label", DefaultValue = "MyBot")]
    public string Label { get; set; }
}