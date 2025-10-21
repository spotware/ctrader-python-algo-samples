using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleLinesTrader : Robot
{
    [Parameter("Volume", Group = "Volume", DefaultValue = 1000, MinValue = 0, Step = 1)]
    public double Volume { get; set; }

    [Parameter("Stop Loss Pips", Group = "Protection", DefaultValue = 0.0, MinValue = 0.0, Step = 1)]
    public double StopLossPips { get; set; }

    [Parameter("Take Profit Pips", Group = "Protection", DefaultValue = 0.0, MinValue = 0.0, Step = 1)]
    public double TakeProfitPips { get; set; }

    [Parameter("Allow trading", Group = "Trading", DefaultValue = true)]
    public bool IsTradingAllowed { get; set; }

    [Parameter("Allow email notifications", Group = "Email notifications", DefaultValue = false)]
    public bool IsEmailAllowed { get; set; }

    [Parameter("Email address", Group = "Email notifications")]
    public string EmailAddress { get; set; }

    [Parameter("Show How To Use", Group = "Settings", DefaultValue = true)]
    public bool ShowHowToUse { get; set; }
}