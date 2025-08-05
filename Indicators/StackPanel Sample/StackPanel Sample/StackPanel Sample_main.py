import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class StackPanelSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.Orientation = api.PanelOrientation

        for i in range(10):
            textBlock = TextBlock()
            textBlock.Text = "Text"
            textBlock.Margin = Thickness(5)
            textBlock.ForegroundColor = Color.Black
            textBlock.FontWeight = FontWeight.ExtraBold
            stackPanel.AddChild(textBlock)


        api.Chart.AddControl(stackPanel)