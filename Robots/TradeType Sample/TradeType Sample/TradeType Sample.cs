using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class TradeTypeSample : Robot
{
    [Parameter("Trade Type", DefaultValue = TradeType.Buy)]
    public TradeType TradeType { get; set; }
}