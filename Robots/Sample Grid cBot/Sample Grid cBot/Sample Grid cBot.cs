using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleGridcBot : Robot
{
    // Define the input parameters for the cBot.
    [Parameter("Volume (lots)", DefaultValue = 0.01, MinValue = 0.01, Step = 0.01)]
    public double VolumeInLots { get; set; }  // Trade volume in lots.

    [Parameter("Trade Side")]
    public TradeType TradeType { get; set; }  // Trade direction (buy or sell).

    [Parameter("Step (pips)", DefaultValue = 5, MinValue = 0.1, Step = 0.1)]
    public double StepPips { get; set; }  // Step size in pips to open the next grid position.

    [Parameter("Target Profit", DefaultValue = 20)]
    public double TargetProfit { get; set; }  // Target profit for the grid in the account currency.
}