import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PenLineCapSample():
    def initialize(self):
        rectangle = Rectangle()
        rectangle.HorizontalAlignment = HorizontalAlignment.Center
        rectangle.VerticalAlignment = VerticalAlignment.Center
        rectangle.StrokeStartLineCap = api.StrokeStartLineCap
        rectangle.StrokeEndLineCap = api.StrokeEndLineCap
        rectangle.StrokeDashCap = api.StrokeDashCap
        rectangle.StrokeColor = Color.Red
        rectangle.StrokeThickness = 4
        rectangle.Width = 200
        rectangle.Height = 100

        api.Chart.AddControl(rectangle)