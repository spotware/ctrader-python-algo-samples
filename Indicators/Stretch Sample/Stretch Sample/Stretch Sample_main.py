import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class StretchSample():
    def initialize(self):
        rectangle = Rectangle()
        rectangle.Stretch = api.Stretch
        rectangle.HorizontalAlignment = HorizontalAlignment.Center
        rectangle.VerticalAlignment = VerticalAlignment.Center
        rectangle.Height = 100
        rectangle.Width = 200
        rectangle.FillColor = Color.Blue
        rectangle.StrokeColor = Color.Red
        rectangle.Opacity = 0.7

        api.Chart.AddControl(rectangle)