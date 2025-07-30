import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CharacterCasingSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.6
        stackPanel.Width = 200

        lowerCasingTextBlock = TextBlock()
        lowerCasingTextBlock.Text = "Lower Character Casing"
        lowerCasingTextBlock.Margin = Thickness(10, 10, 10, 0)
        lowerCasingTextBlock.ForegroundColor = Color.Red
        lowerCasingTextBlock.FontWeight = FontWeight.ExtraBold

        stackPanel.AddChild(lowerCasingTextBlock)

        lowerCasingTextBox = TextBox()
        lowerCasingTextBox.CharacterCasing = CharacterCasing.Lower
        lowerCasingTextBox.Margin = Thickness(10)

        stackPanel.AddChild(lowerCasingTextBox)

        upperCasingTextBlock = TextBlock()
        upperCasingTextBlock.Text = "Upper Character Casing"
        upperCasingTextBlock.Margin = Thickness(10, 10, 10, 0)
        upperCasingTextBlock.ForegroundColor = Color.Red
        upperCasingTextBlock.FontWeight = FontWeight.ExtraBold

        stackPanel.AddChild(upperCasingTextBlock)

        upperCasingTextBox = TextBox()
        upperCasingTextBox.CharacterCasing = CharacterCasing.Upper
        upperCasingTextBox.Margin = Thickness(10)

        stackPanel.AddChild(upperCasingTextBox)

        normalCasingTextBlock = TextBlock()
        normalCasingTextBlock.Text = "Normal Character Casing"
        normalCasingTextBlock.Margin = Thickness(10, 10, 10, 0)
        normalCasingTextBlock.ForegroundColor = Color.Red
        normalCasingTextBlock.FontWeight = FontWeight.ExtraBold

        stackPanel.AddChild(normalCasingTextBlock)

        normalCasingTextBox = TextBox()
        normalCasingTextBox.CharacterCasing = CharacterCasing.Normal
        normalCasingTextBox.Margin = Thickness(10)

        stackPanel.AddChild(normalCasingTextBox)

        api.Chart.AddControl(stackPanel)