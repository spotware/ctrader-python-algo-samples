using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class KeltnerChannelsSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "KeltnerChannelsSample")]
    public string Label { get; set; }

    [Parameter("MA Period", DefaultValue = 20, Group = "Keltner Channels", MinValue = 1)]
    public int MaPeriod { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Keltner Channels")]
    public MovingAverageType MaType { get; set; }

    [Parameter("ATR Period", DefaultValue = 10, Group = "Keltner Channels", MinValue = 1)]
    public int AtrPeriod { get; set; }

    [Parameter("ATR MA Type", DefaultValue = MovingAverageType.Simple, Group = "Keltner Channels")]
    public MovingAverageType AtrMaType { get; set; }

    [Parameter("Band Distance", DefaultValue = 2.0, MinValue = 0)]
    public double BandDistance { get; set; }
}