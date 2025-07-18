using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class DonchianChannelSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "DonchianChannelSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Donchian Channel", MinValue = 1)]
    public int Periods { get; set; }
}