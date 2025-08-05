import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WrapPanelSample():
    def initialize(self):
        wrapPanel = WrapPanel()
        wrapPanel.BackgroundColor = Color.Gold
        wrapPanel.HorizontalAlignment = HorizontalAlignment.Center
        wrapPanel.VerticalAlignment = VerticalAlignment.Center
        wrapPanel.Orientation = api.PanelOrientation

        for i in range(10):
            textBlock = TextBlock()
            textBlock.Text = "Text"
            textBlock.Margin = Thickness(5)
            textBlock.ForegroundColor = Color.Black
            textBlock.FontWeight = FontWeight.ExtraBold
            wrapPanel.AddChild(textBlock)


        api.Chart.AddControl(wrapPanel)