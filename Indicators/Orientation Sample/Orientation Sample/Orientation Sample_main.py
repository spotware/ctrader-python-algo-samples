import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class OrientationSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.Orientation = api.Orientation
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.7

        stackPanel.AddChild(self.get_text_block("First TextBlock"))
        stackPanel.AddChild(self.get_text_block("Second TextBlock"))
        stackPanel.AddChild(self.get_text_block("Third TextBlock"))
        stackPanel.AddChild(self.get_text_block("Fourth TextBlock"))

        api.Chart.AddControl(stackPanel)

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.FontWeight = FontWeight.ExtraBold
        textBlock.Margin = Thickness(5)
        textBlock.ForegroundColor = Color.Black
        return textBlock