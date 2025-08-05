using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.FullAccess, IsOverlay = true)]
public partial class StretchDirectionSample : Indicator
{
    [Parameter("Stretch Direction", DefaultValue = StretchDirection.UpOnly)]
    public StretchDirection StretchDirection { get; set; }
    
    [Parameter("Image File Path")]
    public string ImageFilePath { get; set; }
}
