import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ButtonClickEventArgsSample():
    def initialize(self):
        button = Button()
        button.Text = "Button not clicked yet"
        button.HorizontalAlignment = HorizontalAlignment.Center
        button.VerticalAlignment = VerticalAlignment.Center

        # Whenever you click on the button the Button_Click method will be called
        button.Click += self.buttonClick

        api.Chart.AddControl(button)

    def buttonClick(self, args):
        args.Button.Text = "Button Clicked"