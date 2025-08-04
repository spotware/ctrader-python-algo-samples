import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class RadioButtonEventArgsSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.8

        firstRadioButton = RadioButton()
        firstRadioButton.Text = "Unchecked"

        firstRadioButton.Checked += self.on_radio_button_changed
        firstRadioButton.Unchecked += self.on_radio_button_changed

        stackPanel.AddChild(firstRadioButton);

        secondRadioButton = RadioButton()
        secondRadioButton.Text = "Unchecked"

        secondRadioButton.Checked += self.on_radio_button_changed
        secondRadioButton.Unchecked += self.on_radio_button_changed

        stackPanel.AddChild(secondRadioButton)

        api.Chart.AddControl(stackPanel)

    def on_radio_button_changed(self, args):
        state = "Checked" if args.RadioButton.IsChecked else "Unchecked"
        args.RadioButton.Text = state