import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ControlPropertySample():
    def initialize(self):
        style = Style()

        style.Set(ControlProperty.Margin, Thickness(5))
        style.Set(ControlProperty.ForegroundColor, Color.Blue)
        style.Set(ControlProperty.FontSize, 14)
        style.Set(ControlProperty.Width, 100)

        textBlock = TextBlock()
        textBlock.Text = "Styled Text Block"
        textBlock.Style = style
        textBlock.HorizontalAlignment = HorizontalAlignment.Center
        textBlock.VerticalAlignment = VerticalAlignment.Center

        api.Chart.AddControl(textBlock)