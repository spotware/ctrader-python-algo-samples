using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.FullAccess)]
public partial class SamplecBotReferenceSMA : Robot
{
    [Parameter("Source")]
    public DataSeries Source { get; set; }

    [Parameter("SMA Period", DefaultValue = 14)]
    public int SmaPeriod { get; set; }
}