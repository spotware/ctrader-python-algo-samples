import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class CompilationRobotSample():
    def on_start(self):
        options = CompilationOptions()
        options.IncludeSourceCode = api.IncludeSourceCode
        options.OutputAlgoFilePath = api.OutputAlgoFilePath

        resultSync = api.Compiler.Compile(api.AlgoProjectPath, options);
        api.Print(resultSync.Succeeded);