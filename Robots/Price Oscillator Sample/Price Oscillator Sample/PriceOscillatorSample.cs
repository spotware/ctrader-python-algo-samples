using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PriceOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "PriceOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Price Oscillator")]
    public DataSeries Source { get; set; }

    [Parameter("Long Cycle", DefaultValue = 22, Group = "Price Oscillator", MinValue = 1)]
    public int LongCycle { get; set; }

    [Parameter("Short Cycle", DefaultValue = 14, Group = "Price Oscillator", MinValue = 1)]
    public int ShortCycle { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Price Oscillator")]
    public MovingAverageType MaType { get; set; }
}