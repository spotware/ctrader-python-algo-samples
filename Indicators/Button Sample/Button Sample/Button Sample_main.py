import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ButtonSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.7

        for i in range(5):
            button = Button()
            button.Text = f"Button # {i}"
            button.Margin = Thickness(10)
            button.Click += self.buttonClick
            stackPanel.AddChild(button)

        api.Chart.AddControl(stackPanel)

    def buttonClick(self, args):
        textSplit = args.Button.Text.split()[:3];
        args.Button.Text = f"{" ".join(textSplit)} Clicked";