import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CheckBoxControlSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold

        checkBox = CheckBox()
        checkBox.Text = "Unchecked"
        checkBox.Margin = Thickness(10)
        checkBox.FontWeight = FontWeight.ExtraBold

        checkBox.Checked += self.on_check_box_checked
        checkBox.Unchecked += self.on_check_box_unchecked

        stackPanel.AddChild(checkBox)

        api.Chart.AddControl(stackPanel)

    def on_check_box_checked(self, args):
        args.CheckBox.Text = "Checked"

    def on_check_box_unchecked(self, args):
        args.CheckBox.Text = "Unchecked"