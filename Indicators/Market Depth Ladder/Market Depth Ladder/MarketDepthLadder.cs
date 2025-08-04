using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class MarketDepthLadder : Indicator
{
    [Parameter("Offset", DefaultValue = 20)]
    public int Offset { get; set; }

    [Parameter("Max Length", DefaultValue = 20, Step = 1, MinValue = 0)]
    public double MaxLength { get; set; }

    [Parameter("Buy Orders Color", DefaultValue = "Lime")]
    public Color BuyOrdersColor { get; set; }

    [Parameter("Sell Orders Color", DefaultValue = "Red")]
    public Color SellOrdersColor { get; set; }
}
