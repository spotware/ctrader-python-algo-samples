import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ChartDisplaySettingsSample():
    def on_start(self):
        # Adding an event handler for the DisplaySettingsChanged event
        api.Chart.DisplaySettingsChanged += self.on_chart_display_settings_changed

        api.Chart.DisplaySettings.IndicatorTitles = False

    def on_chart_display_settings_changed(self, args):
        api.Print(f"IndicatorTitles: {args.Chart.DisplaySettings.IndicatorTitles}")