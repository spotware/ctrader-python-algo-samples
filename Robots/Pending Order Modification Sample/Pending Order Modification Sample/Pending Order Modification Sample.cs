using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class PendingOrderModificationSample : Robot
{
    [Parameter("Order Comment")]
    public string OrderComment { get; set; }

    [Parameter("Order Label")]
    public string OrderLabel { get; set; }

    [Parameter("Target Price", DefaultValue = 0.0)]
    public double TargetPrice { get; set; }

    [Parameter("Stop Loss (Pips)", DefaultValue = 10)]
    public double StopLossInPips { get; set; }

    [Parameter("Stop Loss Trigger Method", DefaultValue = StopTriggerMethod.Trade)]
    public StopTriggerMethod StopLossTriggerMethod { get; set; }

    [Parameter("Take Profit (Pips)", DefaultValue = 10)]
    public double TakeProfitInPips { get; set; }

    [Parameter("Expiry (HH:mm:ss)")]
    public string Expiry { get; set; }

    [Parameter("Volume (Lots)", DefaultValue = 0.01)]
    public double VolumeInLots { get; set; }

    [Parameter("Has Trailing Stop", DefaultValue = false)]
    public bool HasTrailingStop { get; set; }

    [Parameter("Order Trigger Method", DefaultValue = StopTriggerMethod.Trade)]
    public StopTriggerMethod OrderTriggerMethod { get; set; }

    [Parameter("Limit Range (Pips)", DefaultValue = 10)]
    public double LimitRangeInPips { get; set; }
}