using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class RSIReversalStrategySample : Robot
{
    [Parameter(DefaultValue = 30)]
    public int BuyLevel { get; set; }

    [Parameter(DefaultValue = 70)]
    public int SellLevel { get; set; }
}