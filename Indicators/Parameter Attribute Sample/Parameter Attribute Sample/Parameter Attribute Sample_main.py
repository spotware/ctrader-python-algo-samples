import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ParameterAttributeSample():
    def initialize(self):
        api.Print(f"DoubleParameter: {api.DoubleParameter}")
        api.Print(f"IntParameter: {api.IntParameter}")
        api.Print(f"BoolParameter: {api.BoolParameter}")
        api.Print(f"StringParameter: {api.StringParameter}")
        api.Print(f"TradeTypeParameter: {api.TradeTypeParameter}")
        api.Print(f"CustomEnumParameter: {api.CustomEnumParameter}")
        api.Print(f"ColorParameter: {api.ColorParameter}")
        api.Print(f"DataSeriesParameter: {api.DataSeriesParameter}")
        api.Print(f"TimeFrameParameter: {api.TimeFrameParameter}")