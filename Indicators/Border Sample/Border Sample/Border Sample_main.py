import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BorderSample():
    def initialize(self):
        border = Border()
        border.BorderColor = Color.Yellow
        border.BorderThickness = Thickness(2)
        border.Opacity = 0.5
        border.BackgroundColor = Color.Violet
        border.HorizontalAlignment = HorizontalAlignment.Center
        border.VerticalAlignment = VerticalAlignment.Center
        border.Width = 200
        border.Height = 100
        border.Margin = Thickness(10)

        stackPanel = StackPanel()
        stackPanel.Orientation = Orientation.Vertical

        textBlock = TextBlock()
        textBlock.Text = "Text"
        textBlock.Margin = Thickness(5)
        textBlock.HorizontalAlignment = HorizontalAlignment.Center
        textBlock.FontWeight = FontWeight.ExtraBold

        stackPanel.AddChild(textBlock)

        button = Button()
        button.Text = "Button"
        button.Margin = Thickness(5)
        button.HorizontalAlignment = HorizontalAlignment.Center
        button.FontWeight = FontWeight.ExtraBold

        stackPanel.AddChild(button);

        textBox = TextBox()
        textBox.Text = "Text"
        textBox.Margin = Thickness(5)
        textBox.HorizontalAlignment = HorizontalAlignment.Center
        textBox.FontWeight = FontWeight.ExtraBold
        textBox.Width = 100

        stackPanel.AddChild(textBox)

        border.Child = stackPanel;

        api.Chart.AddControl(border);