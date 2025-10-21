using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleTrendcBot : Robot
{
    // Define input parameters for the cBot.
    [Parameter("Quantity (Lots)", Group = "Volume", DefaultValue = 1, MinValue = 0.01, Step = 0.01)]
    public double Quantity { get; set; }  // Trade quantity in lots.

    [Parameter("MA Type", Group = "Moving Average")]
    public MovingAverageType MAType { get; set; }  // Type of moving average. 

    [Parameter("Source", Group = "Moving Average")]
    public DataSeries SourceSeries { get; set; }  // Data series to calculate the moving average.

    [Parameter("Slow Periods", Group = "Moving Average", DefaultValue = 10)]
    public int SlowPeriods { get; set; }  // Number of periods for the slow moving average.

    [Parameter("Fast Periods", Group = "Moving Average", DefaultValue = 5)]
    public int FastPeriods { get; set; }  // Number of periods for the fast moving average.
}