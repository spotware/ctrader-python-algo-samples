using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleRSIcBot : Robot
{
    // Define input parameters for the cBot.
    [Parameter("Quantity (Lots)", Group = "Volume", DefaultValue = 1, MinValue = 0.01, Step = 0.01)]
    public double Quantity { get; set; }  // Trade quantity in lots.

    [Parameter("Source", Group = "RSI")]
    public DataSeries Source { get; set; }  // Data series for the RSI indicator.

    [Parameter("Periods", Group = "RSI", DefaultValue = 14)]
    public int Periods { get; set; }  // Number of periods to calculate RSI.
}