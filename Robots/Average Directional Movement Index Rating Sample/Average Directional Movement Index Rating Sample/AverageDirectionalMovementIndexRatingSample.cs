using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class AverageDirectionalMovementIndexRatingSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "AverageDirectionalMovementIndexRatingSample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 14, Group = "Average Directional Movement Index Rating")]
    public int Periods { get; set; }

    [Parameter("ADXR Level", DefaultValue = 25, Group = "Average Directional Movement Index Rating")]
    public int ADXRLevel { get; set; }
}