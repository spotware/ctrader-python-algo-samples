using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TextWrappingSample : Indicator
{
    [Parameter("Text", DefaultValue = "very long texttttttttttttttttttttt")]
    public string Text { get; set; }

    [Parameter("Wrapping", DefaultValue = TextWrapping.NoWrap)]
    public TextWrapping TextWrapping { get; set; }
}
