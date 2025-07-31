import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ColorThemeChangeEventArgsSample():
    def initialize(self):
        api.Application.ColorThemeChanged += self.on_application_color_theme_changed

    def on_application_color_theme_changed(self, args):
        text = f"Theme Changed To: {args.ColorTheme}"
        api.Chart.DrawStaticText("text", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)