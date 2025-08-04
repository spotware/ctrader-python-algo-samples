import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PenLineJoinSample():
    def initialize(self):
        rectangle = Rectangle()
        rectangle.HorizontalAlignment = HorizontalAlignment.Center
        rectangle.VerticalAlignment = VerticalAlignment.Center
        rectangle.StrokeLineJoin = api.StrokeLineJoin
        rectangle.StrokeColor = Color.Red
        rectangle.StrokeThickness = 4
        rectangle.Width = 200
        rectangle.Height = 100

        api.Chart.AddControl(rectangle)