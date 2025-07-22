using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class RainbowOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "RainbowOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Rainbow Oscillator")]
    public DataSeries SourceRainbowOscillator { get; set; }

    [Parameter(MinValue = 2, DefaultValue = 9, Group = "Rainbow Oscillator")]
    public int LevelsRainbowOscillator { get; set; }

    [Parameter("MA Type", DefaultValue = MovingAverageType.Simple, Group = "Rainbow Oscillator")]
    public MovingAverageType MaTypeRainbowOscillator { get; set; }

    [Parameter("Periods", DefaultValue = 9, Group = "Simple Moving Average", MinValue = 0)]
    public int PeriodsSimpleMovingAverage { get; set; }
}