import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ColorSample():
    def initialize(self):
        api.Chart.ColorSettings.BackgroundColor = api.ColorParameter