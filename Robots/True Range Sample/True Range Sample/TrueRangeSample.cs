using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class TrueRangeSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "TrueRangeSample")]
    public string Label { get; set; }
}