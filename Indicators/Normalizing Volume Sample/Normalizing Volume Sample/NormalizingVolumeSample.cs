using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class NormalizingVolumeSample : Indicator
{
    [Parameter("Volume Unit", DefaultValue = VolumeUnit.Units)]
    public VolumeUnit VolumeUnit { get; set; }

    [Parameter("Volume Amount", DefaultValue = 0.01)]
    public double VolumeAmount { get; set; }

    [Parameter("Rounding Mode", DefaultValue = RoundingMode.ToNearest)]
    public RoundingMode RoundingMode { get; set; }
}

public enum VolumeUnit
{
    Units,
    Lots
}