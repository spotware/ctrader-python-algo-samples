import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TextAlignmentSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.Opacity = 0.6
        stackPanel.Width = 200

        textBlock = TextBlock()
        textBlock.Text = "Sample text"
        textBlock.TextAlignment = api.TextAlignment

        stackPanel.AddChild(textBlock)

        api.Chart.AddControl(stackPanel)