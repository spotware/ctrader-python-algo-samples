import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

def getTextBlock(text):
    textBlock = TextBlock()
    textBlock.Text = text
    textBlock.Margin = Thickness(5)
    return textBlock

class ApplicationSample():
    def initialize(self):
        api.Application.ColorThemeChanged += self.applicationColorThemeChanged
        api.Application.UserTimeOffsetChanged += self.applicationUserTimeOffsetChanged
        self.drawApplicationInfo()

    def drawApplicationInfo(self):
        grid = Grid(3, 2)
        grid.BackgroundColor = Color.Goldenrod
        grid.HorizontalAlignment = api.HorizontalAlignment
        grid.VerticalAlignment = api.VerticalAlignment

        grid.AddChild(getTextBlock("Version"), 0, 0)
        grid.AddChild(getTextBlock(str(api.Application.Version)), 0, 1)

        grid.AddChild(getTextBlock("Theme"), 1, 0)

        self.themeTextBlock = getTextBlock(str(api.Application.ColorTheme))

        grid.AddChild(self.themeTextBlock, 1, 1)

        grid.AddChild(getTextBlock("User Time Offset"), 2, 0)

        self.userTimeOffsetTextBlock = getTextBlock(str(api.Application.UserTimeOffset))

        grid.AddChild(self.userTimeOffsetTextBlock, 2, 1)

        api.Chart.AddControl(grid)

    def applicationUserTimeOffsetChanged(self, obj):
        self.userTimeOffsetTextBlock.Text = str(obj.UserTimeOffset)

    def applicationColorThemeChanged(self, obj):
        self.themeTextBlock.Text = str(obj.ColorTheme)