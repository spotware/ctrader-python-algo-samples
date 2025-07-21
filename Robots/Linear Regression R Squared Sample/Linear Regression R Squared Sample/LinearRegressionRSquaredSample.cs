using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class LinearRegressionRSquaredSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "LinearRegressionRSquaredSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Linear Regression")]
    public DataSeries SourceLinearRegression { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Linear Regression", MinValue = 0)]
    public int PeriodsLinearRegression { get; set; }

    [Parameter("Source", Group = "Simple Moving Average")]
    public DataSeries SourceSimpleMovingAverage { get; set; }

    [Parameter("Periods", DefaultValue = 10, Group = "Simple Moving Average", MinValue = 0)]
    public int PeriodsSimpleMovingAverage { get; set; }

    [Parameter("Source", Group = "Exponential Moving Average")]
    public DataSeries SourceExponentialMovingAverage { get; set; }

    [Parameter("Periods", DefaultValue = 20, Group = "Exponential Moving Average", MinValue = 0)]
    public int PeriodsExponentialMovingAverage { get; set; }
}