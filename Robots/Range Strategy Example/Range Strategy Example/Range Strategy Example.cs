using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class RangeStrategyExample : Robot
{
    [Parameter(DefaultValue = 100000)]
    public double Volume { get; set; }

    [Parameter(DefaultValue = 20)]
    public double StopLoss { get; set; }

    [Parameter(DefaultValue = 20)]
    public double TakeProfit { get; set; }
}