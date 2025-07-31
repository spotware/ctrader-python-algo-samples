import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ControlAlignmentSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = api.HorizontalAlignment
        stackPanel.VerticalAlignment = api.VerticalAlignment
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.6
        stackPanel.Width = 200
        stackPanel.Height = 100

        api.Chart.AddControl(stackPanel)