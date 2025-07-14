using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class ChaikinVolatilitySample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "ChaikinVolatilitySample")]
    public string Label { get; set; }

    [Parameter(DefaultValue = 14, Group = "Chaikin Volatility", MinValue = 1)]
    public int ChaikinPeriods { get; set; }

    [Parameter("Rate of Change", DefaultValue = 10, Group = "Chaikin Volatility", MinValue = 0)]
    public int RateOfChange { get; set; }

    [Parameter("MA Type Chaikin", Group = "Chaikin Volatility")]
    public MovingAverageType MaTypeChaikin { get; set; }

    [Parameter(DefaultValue = 14, Group = "Moving Average", MinValue = 1)]
    public int SmaPeriods { get; set; }

    [Parameter("MA Type", Group = "Moving Average")]
    public MovingAverageType MaType { get; set; }
}