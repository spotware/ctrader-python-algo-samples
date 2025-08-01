using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.FullAccess, IsOverlay = true)]
public partial class ImageSample : Indicator
{
    [Parameter("Image File Path")]
    public string ImageFilePath { get; set; }
}
