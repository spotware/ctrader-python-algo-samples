using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PendingOrdersSample : Robot
{
    [Parameter("Label", DefaultValue = "MyOrders")]
    public string Label { get; set; }
}