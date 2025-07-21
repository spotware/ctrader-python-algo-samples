using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class ParabolicSarSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "ParabolicSARSample")]
    public string Label { get; set; }

    [Parameter("Min AF", DefaultValue = 0.02, Group = "Parabolic SAR", MinValue = 0)]
    public double MinAf { get; set; }

    [Parameter("Max AF", DefaultValue = 0.2, Group = "Parabolic SAR", MinValue = 0)]
    public double MaxAf { get; set; }
}