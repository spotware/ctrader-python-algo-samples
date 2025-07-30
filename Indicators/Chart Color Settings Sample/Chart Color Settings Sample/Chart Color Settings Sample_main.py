import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartColorSettingsSample():
    def initialize(self):
        grid = Grid(10, 2)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Left
        grid.VerticalAlignment = VerticalAlignment.Bottom

        self.style = Style()

        self.style.Set(ControlProperty.Margin, 5)
        self.style.Set(ControlProperty.FontWeight, FontWeight.ExtraBold)
        self.style.Set(ControlProperty.ForegroundColor, Color.Red)
        self.style.Set(ControlProperty.MinWidth, 100)

        grid.AddChild(self.get_text_block("Ask Price Line Color"), 0, 0)

        self.askPriceLineColorTextBox = self.get_text_box(api.Chart.ColorSettings.AskPriceLineColor.ToHexString())

        grid.AddChild(self.askPriceLineColorTextBox, 0, 1)

        grid.AddChild(self.get_text_block("Bid Price Line Color"), 1, 0)

        self.bidPriceLineColorTextBox = self.get_text_box(api.Chart.ColorSettings.BidPriceLineColor.ToHexString())

        grid.AddChild(self.bidPriceLineColorTextBox, 1, 1);

        grid.AddChild(self.get_text_block("Background Color"), 2, 0);

        self.backgroundColorTextBox = self.get_text_box(api.Chart.ColorSettings.BackgroundColor.ToHexString())

        grid.AddChild(self.backgroundColorTextBox, 2, 1);

        changeButton = Button()
        changeButton.Text = "Change"
        changeButton.Style = self.style

        changeButton.Click += self.on_change_button_click

        grid.AddChild(changeButton, 9, 0);

        api.Chart.AddControl(grid);

    def on_change_button_click(self, args):
        api.Chart.ColorSettings.AskPriceLineColor = self.get_color(self.askPriceLineColorTextBox.Text)
        api.Chart.ColorSettings.BidPriceLineColor = self.get_color(self.bidPriceLineColorTextBox.Text)
        api.Chart.ColorSettings.BackgroundColor = self.get_color(self.backgroundColorTextBox.Text)

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock

    def get_text_box(self, text):
        textBlock = TextBox()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock

    def get_color(self, colorNameOrHex):
        return Color.FromHex(colorNameOrHex) if colorNameOrHex[0] == '#' else Color.FromName(colorNameOrHex)