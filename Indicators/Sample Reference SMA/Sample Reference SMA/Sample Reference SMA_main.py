import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

'''
To reference another custom indicator you have to:
0. Build the custom indicator you want to reference, it will output a DLL file in indicator bin directory
1. Reference the custom indicator DLL file in your indicator project (csproj) file, check this indicator project file as an example.
2. Load custom indicator assembly in your indicator main C# file, check this indicator Engine.cs C# file (Line 17) as an example
3. Add below line to load the custom indicator assembly

This is a workaround and we will provide better solution in future for referencing custom indicators in your Python algo.
'''

clr.AddReference("Sample SMA")

# Import custom indicator type by it's namespace
# If namespace is different then change the 'cAlgo.Indicators' to indicator type namespace
from cAlgo.Indicators import SampleSMA

class SampleReferenceSMA():
    def initialize(self):
        # Save current indicator output as when loading referenced indicator will change the context
        self.RefSMA = api.RefSMA
        self.sma = api.Indicators.GetIndicator[SampleSMA](api.Source, api.SmaPeriod)
        
    def calculate(self, index):
        self.RefSMA[index] = self.sma.Result[index]