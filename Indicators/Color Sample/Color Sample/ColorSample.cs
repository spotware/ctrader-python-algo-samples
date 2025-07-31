using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public partial class ColorSample : Indicator
{
    [Parameter("Color", DefaultValue = "#168565")]
    public Color ColorParameter { get; set; }
}