using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class SampleTradingPanel : Robot
{
    [Parameter("Vertical Position", Group = "Panel alignment", DefaultValue = VerticalAlignment.Top)]
    public VerticalAlignment PanelVerticalAlignment { get; set; }

    [Parameter("Horizontal Position", Group = "Panel alignment", DefaultValue = HorizontalAlignment.Left)]
    public HorizontalAlignment PanelHorizontalAlignment { get; set; }

    [Parameter("Default Lots", Group = "Default trade parameters", DefaultValue = 0.01)]
    public double DefaultLots { get; set; }

    [Parameter("Default Take Profit (pips)", Group = "Default trade parameters", DefaultValue = 20)]
    public double DefaultTakeProfitPips { get; set; }

    [Parameter("Default Stop Loss (pips)", Group = "Default trade parameters", DefaultValue = 20)]
    public double DefaultStopLossPips { get; set; }
}