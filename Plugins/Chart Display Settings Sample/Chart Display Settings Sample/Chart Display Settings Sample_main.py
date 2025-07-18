import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartDisplaySettingsSample():
    def on_start(self):
        # Creating a new Chart for EURUSD on plugin start
        # You can also use existing charts via ChartManager
        self.newChart = api.ChartManager.AddChartFrame("EURUSD", TimeFrame.Daily).Chart
            
        # Adding an event handler for the DisplaySettingsChanged event
        self.newChart.DisplaySettingsChanged += self.on_chart_display_settings_changed

        self.newChart.DisplaySettings.IndicatorTitles = False

    def on_chart_display_settings_changed(self, args):
        api.Print(f"IndicatorTitles: {args.Chart.DisplaySettings.IndicatorTitles}")
