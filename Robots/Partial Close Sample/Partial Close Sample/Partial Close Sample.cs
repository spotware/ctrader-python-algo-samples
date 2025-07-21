using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PartialCloseSample : Robot
{
    [Parameter("Close %", DefaultValue = 20, Group = "First Level")]
    public double FirstLevelCloseAmountInPercentage { get; set; }

    [Parameter("Pips", DefaultValue = 20, Group = "First Level")]
    public double FirstLevelClosePips { get; set; }

    [Parameter("Close %", DefaultValue = 20, Group = "Second Level")]
    public double SecondLevelCloseAmountInPercentage { get; set; }

    [Parameter("Pips", DefaultValue = 35, Group = "Second Level")]
    public double SecondLevelClosePips { get; set; }
}