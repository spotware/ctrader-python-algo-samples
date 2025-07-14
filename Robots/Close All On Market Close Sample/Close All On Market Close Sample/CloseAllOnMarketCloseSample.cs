using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class CloseAllOnMarketCloseSample : Robot
{
    [Parameter("Close Before", DefaultValue = "00:05:00")]
    public string CloseBeforeTime { get; set; }
}