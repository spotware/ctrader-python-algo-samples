using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TextAlignmentSample : Indicator
{
    [Parameter("Text Alignment", DefaultValue = TextAlignment.Center)]
    public TextAlignment TextAlignment { get; set; }
}
