import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ThicknessSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.6

        rectangle = Rectangle()
        rectangle.HorizontalAlignment = HorizontalAlignment.Center
        rectangle.VerticalAlignment = VerticalAlignment.Center
        rectangle.StrokeThickness = 2
        rectangle.Margin = Thickness(10, 5, 10, 5)
        rectangle.Width = 300
        rectangle.Height = 100
        rectangle.FillColor = Color.Red
        rectangle.StrokeColor = Color.Blue

        stackPanel.AddChild(rectangle)
        
        api.Chart.AddControl(stackPanel)