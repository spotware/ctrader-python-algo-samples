using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None)]
public partial class SampleAdvancedTakeProfit : Robot
{
    [Parameter("Position Id", Group = "Position")]
    public string PositionId { get; set; }

    [Parameter("Enabled", Group = "Take Profit 1", DefaultValue = false)]
    public bool TakeProfit1Enabled { get; set; }

    [Parameter("Pips", Group = "Take Profit 1", DefaultValue = 10)]
    public double TakeProfit1Pips { get; set; }

    [Parameter("Volume", Group = "Take Profit 1", DefaultValue = 1000)]
    public int TakeProfit1Volume { get; set; }

    [Parameter("Enabled", Group = "Take Profit 2", DefaultValue = false)]
    public bool TakeProfit2Enabled { get; set; }

    [Parameter("Pips", Group = "Take Profit 2", DefaultValue = 20)]
    public double TakeProfit2Pips { get; set; }

    [Parameter("Volume", Group = "Take Profit 2", DefaultValue = 2000)]
    public int TakeProfit2Volume { get; set; }

    [Parameter("Enabled", Group = "Take Profit 3", DefaultValue = false)]
    public bool TakeProfit3Enabled { get; set; }

    [Parameter("Pips", Group = "Take Profit 3", DefaultValue = 10)]
    public double TakeProfit3Pips { get; set; }

    [Parameter("Volume", Group = "Take Profit 3", DefaultValue = 3000)]
    public int TakeProfit3Volume { get; set; }
}