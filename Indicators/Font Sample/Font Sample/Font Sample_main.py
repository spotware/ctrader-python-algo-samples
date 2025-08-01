import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FontSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.6

        stackPanel.AddChild(self.get_text_block("Thin Weight Size 10 FontStyle Normal Font Default", 10, FontWeight.Thin, FontStyle.Normal))
        stackPanel.AddChild(self.get_text_block("Thin Weight Size 10 FontStyle Italic Font Default", 10, FontWeight.Thin, FontStyle.Italic))
        stackPanel.AddChild(self.get_text_block("Thin Weight Size 10 FontStyle Oblique Font Default", 10, FontWeight.Thin, FontStyle.Oblique))
        stackPanel.AddChild(self.get_text_block("Black Weight Size 10 FontStyle Normal Font Default", 10, FontWeight.Black, FontStyle.Normal))
        stackPanel.AddChild(self.get_text_block("Bold Weight Size 10 FontStyle Normal Font Default", 10, FontWeight.Bold, FontStyle.Normal))
        stackPanel.AddChild(self.get_text_block("Heavy Weight Size 10 FontStyle Normal Font Default", 10, FontWeight.Heavy, FontStyle.Normal))
        stackPanel.AddChild(self.get_text_block("Bold Weight Size 12 FontStyle Normal Font Default", 12, FontWeight.Bold, FontStyle.Normal))
        stackPanel.AddChild(self.get_text_block("Thin Weight Size 12 FontStyle Normal Font Calibri Light Italic", 12, FontWeight.Thin, FontStyle.Normal, "Calibri Light Italic"))

        api.Chart.AddControl(stackPanel)

    def get_text_block(self, text, fontSize, fontWeight, fontStyle, fontFamily = None):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.FontSize = fontSize
        textBlock.FontWeight = fontWeight
        textBlock.FontStyle = fontStyle
        textBlock.Margin = Thickness(10)
        textBlock.ForegroundColor = Color.Black
        if fontFamily is not None:
            textBlock.FontFamily = fontFamily
        return textBlock