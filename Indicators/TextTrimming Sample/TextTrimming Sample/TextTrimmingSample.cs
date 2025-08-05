using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TextTrimmingSample : Indicator
{
    [Parameter("Text", DefaultValue = "very long texttttttttttttttttttttt")]
    public string Text { get; set; }
    
    [Parameter("Trimming", DefaultValue = TextTrimming.CharacterEllipsis)]
    public TextTrimming TextTrimming { get; set; }
}
