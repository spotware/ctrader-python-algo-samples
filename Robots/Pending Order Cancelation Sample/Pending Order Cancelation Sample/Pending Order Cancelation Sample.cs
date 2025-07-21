using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PendingOrderCancelationSample : Robot
{
    [Parameter("Order Comment")]
    public string OrderComment { get; set; }

    [Parameter("Order Label")]
    public string OrderLabel { get; set; }
}