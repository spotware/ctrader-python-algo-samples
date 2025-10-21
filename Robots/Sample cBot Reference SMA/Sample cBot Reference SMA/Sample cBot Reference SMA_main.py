import clr

clr.AddReference("cAlgo.API")

'''
To reference another custom indicator you have to:
0. Add its .NET (csproj) file to your indicator solution via an IDE (ex: VisualStudio, Rider, etc...)
1. Reference it in your indicator project (csproj) file, check this indicator project file as an example.
2. Set your algo access rights to FullAccess so your indicator be able to load the assembly file
of custom indicator.
3. Add below line to load the custom indicator assembly, the path to indicator DLL file must be absolute path not relative.  
'''

clr.AddReference(r"C:\Users\afhac\Documents\cAlgo\Sources\Indicators\SampleSMA\SampleSMA\bin\Debug\net6.0\SampleSMA.dll")

# Import cAlgo API types
from cAlgo.API import *
# Import custom indicator type by it's namespace
# If namespace is different then change the 'cAlgo.Indicators' to indicator type namespace
from cAlgo.Indicators import *

# Import trading wrapper functions
from robot_wrapper import *

class SamplecBotReferenceSMA():
    def on_start(self):
        self.sma = api.Indicators.GetIndicator[SampleSMA](api.Source, api.SmaPeriod)

    def on_tick(self):
        api.Print(f"Indicator Result Last Value: {self.sma.Result.LastValue}")