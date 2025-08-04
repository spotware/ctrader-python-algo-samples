import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PolylineSample():
    def initialize(self):
        polyline = Polyline()
        polyline.HorizontalAlignment = HorizontalAlignment.Center
        polyline.VerticalAlignment = VerticalAlignment.Center
        polyline.StrokeColor = Color.Red
        polyline.StrokeThickness = 1
        polyline.Points = [Point(10, 10), Point(100, 200), Point(10, 100), Point(10, 10)]

        api.Chart.AddControl(polyline)