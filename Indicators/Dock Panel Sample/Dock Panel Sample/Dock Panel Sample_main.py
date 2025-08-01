import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class DockPanelSample():
    def initialize(self):
        dockPanel = DockPanel()
        dockPanel.HorizontalAlignment = HorizontalAlignment.Center
        dockPanel.VerticalAlignment = VerticalAlignment.Center
        dockPanel.BackgroundColor = Color.Gold
        dockPanel.Opacity = 0.8

        nameTextBlock = TextBlock()
        nameTextBlock.Text = "Enter Your Name"
        nameTextBlock.Dock = Dock.Top
        nameTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        nameTextBlock.ForegroundColor = Color.Black
        nameTextBlock.FontWeight = FontWeight.ExtraBold

        dockPanel.AddChild(nameTextBlock)

        nameTextBox = TextBox()
        nameTextBox.Dock = Dock.Bottom
        nameTextBox.Margin = Thickness(5)
        nameTextBox.Width = 100

        dockPanel.AddChild(nameTextBox)

        api.Chart.AddControl(dockPanel)