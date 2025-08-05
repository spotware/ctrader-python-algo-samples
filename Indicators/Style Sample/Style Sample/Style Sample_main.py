import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class StyleSample():
    def initialize(self):
        style = Style()

        style.Set(ControlProperty.Margin, Thickness(5))
        style.Set(ControlProperty.ForegroundColor, Color.Blue)
        style.Set(ControlProperty.FontSize, 14)
        style.Set(ControlProperty.Width, 100)

        stackPanel = StackPanel()
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.Orientation = Orientation.Vertical

        for i in range(10):
            textBlock = TextBlock()
            textBlock.Text = f"Text Block #: {i}"
            textBlock.Style = style
            stackPanel.AddChild(textBlock)


        api.Chart.AddControl(stackPanel)