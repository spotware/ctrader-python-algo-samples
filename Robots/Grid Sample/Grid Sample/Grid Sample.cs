using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class GridSample : Robot
{
    [Parameter("Volume (lots)", DefaultValue = 0.01, MinValue = 0.01, Step = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Trade Side")]
    public TradeType TradeType { get; set; }

    [Parameter("Step (pips)", DefaultValue = 5, MinValue = 0.1, Step = 0.1)]
    public double StepPips { get; set; }

    [Parameter("Target Profit", DefaultValue = 20)]
    public double TargetProfit { get; set; }
}