using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class AverageTrueRangeSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "AverageTrueRangeSample")]
    public string Label { get; set; }

    [Parameter(DefaultValue = 14, Group = "Average True Range", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Average True Range")]
    public MovingAverageType MaType { get; set; }
}