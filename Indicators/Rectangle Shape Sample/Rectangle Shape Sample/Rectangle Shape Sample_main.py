import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class RectangleShapeSample():
    def initialize(self):
        rectangle = Rectangle()
        rectangle.HorizontalAlignment = HorizontalAlignment.Center
        rectangle.VerticalAlignment = VerticalAlignment.Center
        rectangle.Width = 200
        rectangle.Height = 150
        rectangle.RadiusX = 20
        rectangle.RadiusY = 20
        rectangle.FillColor = Color.FromArgb(100, Color.Red)
        rectangle.StrokeColor = Color.Yellow

        api.Chart.AddControl(rectangle)