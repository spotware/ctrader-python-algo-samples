import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ToggleButtonSample():
    def initialize(self):
        stackPanel = StackPanel() 
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.7

        for i in range(5):
            toggleButton = ToggleButton()
            toggleButton.Text = f"Toggle Button # {i} Unchecked"
            toggleButton.Margin = Thickness(10)

            toggleButton.Checked += self.on_toggle_button_checked
            toggleButton.Unchecked += self.on_toggle_button_unchecked

            stackPanel.AddChild(toggleButton)

        api.Chart.AddControl(stackPanel)

    def on_toggle_button_checked(self, args):
        textSplit = args.ToggleButton.Text.split()[:4]

        args.ToggleButton.Text = f"{" ".join(textSplit)} Checked"

    def on_toggle_button_unchecked(self, args):
        textSplit = args.ToggleButton.Text.split()[:4]

        args.ToggleButton.Text = f"{" ".join(textSplit)} Unchecked"