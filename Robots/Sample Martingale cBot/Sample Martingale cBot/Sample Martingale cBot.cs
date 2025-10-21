using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleMartingalecBot : Robot
{
    // Define the input parameters for the cBot.
    [Parameter("Initial Quantity (Lots)", Group = "Volume", DefaultValue = 1, MinValue = 0.01, Step = 0.01)]
    public double InitialQuantity { get; set; }  // Initial trade quantity in lots.

    [Parameter("Stop Loss", Group = "Protection", DefaultValue = 40)]
    public int StopLoss { get; set; }  // Stop loss in pips.

    [Parameter("Take Profit", Group = "Protection", DefaultValue = 40)]
    public int TakeProfit { get; set; }  // Take profit in pips.
}