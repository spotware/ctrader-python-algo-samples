using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class MovingAverageSample : Robot
{
    [Parameter("Source", Group = "Fast MA")]
    public DataSeries FastMaSource { get; set; }

    [Parameter("Period", DefaultValue = 9, Group = "Fast MA")]
    public int FastMaPeriod { get; set; }

    [Parameter("Type", DefaultValue = MovingAverageType.Exponential, Group = "Fast MA")]
    public MovingAverageType FastMaType { get; set; }

    [Parameter("Source", Group = "Slow MA")]
    public DataSeries SlowMaSource { get; set; }

    [Parameter("Period", DefaultValue = 20, Group = "Slow MA")]
    public int SlowMaPeriod { get; set; }

    [Parameter("Type", DefaultValue = MovingAverageType.Exponential, Group = "Slow MA")]
    public MovingAverageType SlowMaType { get; set; }

    [Parameter("Volume (Lots)", DefaultValue = 0.01, Group = "Trade")]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "MovingAverageSample", Group = "Trade")]
    public string Label { get; set; }
}