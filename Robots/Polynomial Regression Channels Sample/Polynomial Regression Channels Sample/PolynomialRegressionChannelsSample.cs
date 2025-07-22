using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PolynomialRegressionChannelsSample : Robot
{
    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Label", DefaultValue = "PolynomialRegressionChannelsSample")]
    public string Label { get; set; }

    [Parameter("Source", Group = "Polynomial Regression Channels")]
    public DataSeries Source { get; set; }

    [Parameter(DefaultValue = 3.0, Group = "Polynomial Regression Channels", MinValue = 1, MaxValue = 4)]
    public int Degree { get; set; }

    [Parameter(DefaultValue = 120, Group = "Polynomial Regression Channels", MinValue = 1)]
    public int Periods { get; set; }

    [Parameter("Standard Deviation", DefaultValue = 1.62, Group = "Polynomial Regression Channels", Step = 0.01)]
    public double StandardDeviation { get; set; }

    [Parameter("Standard Deviation 2", DefaultValue = 2, Group = "Polynomial Regression Channels", Step = 0.01)]
    public double StandardDeviation2 { get; set; }
}