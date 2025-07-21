using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PatternsStrategySample : Robot
{
    [Parameter(DefaultValue = 1000)]
    public double Volume { get; set; }

    [Parameter(DefaultValue = 10)]
    public double StopLoss { get; set; }

    [Parameter(DefaultValue = 10)]
    public double TakeProfit { get; set; }
}