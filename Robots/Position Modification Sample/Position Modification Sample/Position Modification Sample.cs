using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PositionModificationSample : Robot
{
    [Parameter("Position Comment")]
    public string PositionComment { get; set; }

    [Parameter("Position Label")]
    public string PositionLabel { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10)]
    public double StopLossInPips { get; set; }

    [Parameter("Stop Loss Trigger Method", DefaultValue = StopTriggerMethod.Trade)]
    public StopTriggerMethod StopLossTriggerMethod { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Has Trailing Stop", DefaultValue = false)]
    public bool HasTrailingStop { get; set; }
}