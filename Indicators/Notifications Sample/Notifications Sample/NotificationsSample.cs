using System;
using cAlgo.API;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
public partial class NotificationsSample : Indicator
{
    [Parameter("Sound File Path", DefaultValue = "C:\\Windows\\Media\\notify.wav")]
    public string SoundFilePath { get; set; }

    [Parameter("Sender Email")]
    public string SenderEmail { get; set; }

    [Parameter("Receiver Email")]
    public string ReceiverEmail { get; set; }
    
    [Parameter("Show Popup", DefaultValue = true)]
    public bool ShowPopup { get; set; }
}
