import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CheckBoxEventArgsSample():
    def initialize(self):
        checkBox = CheckBox()
        checkBox.Text = "Check Box"
        checkBox.HorizontalAlignment = HorizontalAlignment.Center
        checkBox.VerticalAlignment = VerticalAlignment.Center

        checkBox.Click += self.on_check_box_click

        api.Chart.AddControl(checkBox)

    def on_check_box_click(self, args):
        state = "Checked" if args.CheckBox.IsChecked else "Unchecked"
        args.CheckBox.Text = state