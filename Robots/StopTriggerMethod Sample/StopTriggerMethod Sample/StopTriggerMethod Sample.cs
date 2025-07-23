using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class StopTriggerMethodSample : Robot
{
    [Parameter("Stop Trigger Method", DefaultValue = StopTriggerMethod.Trade)]
    public StopTriggerMethod StopTriggerMethod { get; set; }
}