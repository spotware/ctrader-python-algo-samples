using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class DirectionalMovementSystemSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "DirectionalMovementSystemSample")]
    public string Label { get; set; }

    [Parameter(DefaultValue = 14, Group = "Directional Movement System", MinValue = 1, MaxValue = 10000)]
    public int Periods { get; set; }

    [Parameter("ADX Level", DefaultValue = 25, Group = "Directional Movement System")]
    public int AdxLevel { get; set; }
}