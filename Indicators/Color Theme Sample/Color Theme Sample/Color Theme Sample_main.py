import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ColorThemeSample():
    def initialize(self):
        self.change_chart_background_color_based_on_theme()
        api.Application.ColorThemeChanged += lambda _: self.change_chart_background_color_based_on_theme()

    def change_chart_background_color_based_on_theme(self):
        api.Chart.ColorSettings.BackgroundColor = Color.White if api.Application.ColorTheme == ColorTheme.Dark else Color.Black