using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None)]
public partial class SampleBreakoutcBot : Robot
{
    // Define the input parameters for the cBot.
    [Parameter("Quantity (Lots)", Group = "Volume", DefaultValue = 1, MinValue = 0.01, Step = 0.01)]
    public double Quantity { get; set; }  // Trade quantity in lots.

    [Parameter("Stop Loss (pips)", Group = "Protection", DefaultValue = 20, MinValue = 1)]
    public int StopLossInPips { get; set; }  // Stop loss in pips.

    [Parameter("Take Profit (pips)", Group = "Protection", DefaultValue = 40, MinValue = 1)]
    public int TakeProfitInPips { get; set; }  // Take profit in pips.

    [Parameter("Source", Group = "Bollinger Bands")]
    public DataSeries Source { get; set; }  // Data series for Bollinger Bands.

    [Parameter("Band Height (pips)", Group = "Bollinger Bands", DefaultValue = 40.0, MinValue = 0)]
    public double BandHeightPips { get; set; }  // Height of Bollinger Bands in pips for a breakout signal.

    [Parameter("Bollinger Bands Deviations", Group = "Bollinger Bands", DefaultValue = 2)]
    public double Deviations { get; set; }  // Deviation value for Bollinger Bands.

    [Parameter("Bollinger Bands Periods", Group = "Bollinger Bands", DefaultValue = 20)]
    public int Periods { get; set; }  // Number of periods for Bollinger Bands.

    [Parameter("Bollinger Bands MA Type", Group = "Bollinger Bands")]
    public MovingAverageType MAType { get; set; }  // Moving average type for Bollinger Bands.

    [Parameter("Consolidation Periods", Group = "Bollinger Bands", DefaultValue = 2)]
    public int ConsolidationPeriods { get; set; }  // Number of consolidation periods required for a breakout signal.
}