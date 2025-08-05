import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TextBoxSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.Opacity = 0.6
        stackPanel.Width = 200

        textBox = TextBox()
        textBox.Text = "Enter text here..."
        textBox.Margin = Thickness(5)
        textBox.ForegroundColor = Color.White
        textBox.HorizontalAlignment = HorizontalAlignment.Center
        textBox.Width = 150

        textBox.TextChanged += self.on_text_box_changed

        stackPanel.AddChild(textBox)

        api.Chart.AddControl(stackPanel)

    def on_text_box_changed(self, args):
        api.Print(f"Text box text changed to: {args.TextBox.Text}")