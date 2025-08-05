using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class TextBlockSample : Indicator
{
    [Parameter("Text", DefaultValue = "Sample text")]
    public string Text { get; set; }
}
