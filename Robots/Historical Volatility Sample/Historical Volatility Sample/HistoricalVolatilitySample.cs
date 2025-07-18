using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class HistoricalVolatilitySample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "HistoricalVolatilitySample")]
    public string Label { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Historical Volatility", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Bar History", DefaultValue = 252, Group = "Historical Volatility")]
    public int BarHistory { get; set; }
}