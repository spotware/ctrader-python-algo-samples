using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None)]
public partial class SampleBreakEven : Robot
{
    [Parameter("Position Id")]
    public string PositionId { get; set; }

    [Parameter("Add Pips", DefaultValue = 0.0, MinValue = 0.0)]
    public double AddPips { get; set; }

    [Parameter("Trigger Pips", DefaultValue = 10, MinValue = 1)]
    public double TriggerPips { get; set; }
}