using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleSARTrailingStop : Robot
{
    [Parameter("Quantity (Lots)", Group = "Volume", DefaultValue = 1, MinValue = 0.01, Step = 0.01)]
    public double Quantity { get; set; }

    [Parameter("Min AF", Group = "Parabolic SAR", DefaultValue = 0.02, MinValue = 0)]
    public double MinAF { get; set; }

    [Parameter("Max AF", Group = "Parabolic SAR", DefaultValue = 0.2, MinValue = 0)]
    public double MaxAF { get; set; }
}