using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class MacdCrossOverSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "MacdCrossOverSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "MACD Crossover")]
    public DataSeries Source { get; set; }

    [Parameter("Long Cycle", DefaultValue = 26, Group = "MACD Crossover", MinValue = 1)]
    public int LongCycle { get; set; }

    [Parameter("Short Cycle", DefaultValue = 12, Group = "MACD Crossover", MinValue = 1)]
    public int ShortCycle { get; set; }

    [Parameter("Signal Periods", DefaultValue = 9, Group = "MACD Crossover", MinValue = 1)]
    public int SignalPeriods { get; set; }
}