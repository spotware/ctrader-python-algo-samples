using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class LinearRegressionInterceptSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double StopLossInPips { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10, MaxValue = 100, MinValue = 1, Step = 1)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Label", DefaultValue = "LinearRegressionInterceptSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Linear Regression Intercept")]
    public DataSeries Source { get; set; }

    [Parameter("Periods", DefaultValue = 9, Group = "Linear Regression Intercept", MinValue = 0)]
    public int Periods { get; set; }
}