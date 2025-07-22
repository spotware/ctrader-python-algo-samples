using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PositionExecutionSample : Robot
{
    [Parameter("Direction", DefaultValue = TradeType.Buy)]
    public TradeType Direction { get; set; }

    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Distance (Pips)", DefaultValue = 20, MinValue = 1)]
    public double DistanceInPips { get; set; }

    [Parameter("Stop (Pips)", DefaultValue = 10, MinValue = 0)]
    public double StopInPips { get; set; }

    [Parameter("Target (Pips)", DefaultValue = 10, MinValue = 0)]
    public double TargetInPips { get; set; }

    [Parameter("Label")]
    public string Label { get; set; }

    [Parameter("Comment")]
    public string Comment { get; set; }

    [Parameter("Trailing Stop", DefaultValue = false)]
    public bool HasTrailingStop { get; set; }

    [Parameter("Stop Loss Trigger Method", DefaultValue = StopTriggerMethod.Trade)]
    public StopTriggerMethod StopLossTriggerMethod { get; set; }

    [Parameter("Async", DefaultValue = false)]
    public bool IsAsync { get; set; }
}