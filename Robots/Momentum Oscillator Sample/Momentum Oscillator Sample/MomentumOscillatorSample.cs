using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class MomentumOscillatorSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "MomentumOscillatorSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Momentum Oscillator")]
    public DataSeries Source { get; set; }

    [Parameter("Periods", DefaultValue = 14, Group = "Momentum Oscillator", MinValue = 1)]
    public int PeriodsMomentumOscillator { get; set; }

    [Parameter("Periods", DefaultValue = 14, Group = "Simple Moving Average", MinValue = 0)]
    public int PeriodsSimpleMovingAverage { get; set; }
}