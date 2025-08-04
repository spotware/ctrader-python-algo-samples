import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class RadioButtonSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.8

        firstRadioButton = RadioButton()
        firstRadioButton.Text = "Unchecked"

        firstRadioButton.Checked += self.on_radio_button_checked
        firstRadioButton.Unchecked += self.on_radio_button_unchecked

        stackPanel.AddChild(firstRadioButton);

        secondRadioButton = RadioButton()
        secondRadioButton.Text = "Unchecked"

        secondRadioButton.Checked += self.on_radio_button_checked
        secondRadioButton.Unchecked += self.on_radio_button_unchecked

        stackPanel.AddChild(secondRadioButton)

        api.Chart.AddControl(stackPanel)

    def on_radio_button_checked(self, args):
        radioButton = args.RadioButton
        radioButton.Text = "Checked"

    def on_radio_button_unchecked(self, args):
        radioButton = args.RadioButton
        radioButton.Text = "Unchecked"