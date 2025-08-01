import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IndicatorTitlesSample():
    def initialize(self):
        # Adding a custom event handler for the DisplaySettingsChanged event
        api.Chart.DisplaySettingsChanged += self.on_display_settings_changed    
        api.Print(str(api.Chart.DisplaySettings.IndicatorTitles))
    def on_display_settings_changed(self, args):
        api.Print(str(api.Chart.DisplaySettings.IndicatorTitles))