using cAlgo.API;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public partial class CompilationRobotSample : Robot
{
    [Parameter("Algo Project Path")]
    public string AlgoProjectPath { get; set; }
    
    [Parameter("Output Algo File Path")]
    public string OutputAlgoFilePath { get; set; }
    
    [Parameter("Include Source Code", DefaultValue = true)]
    public bool IncludeSourceCode { get; set; }
}