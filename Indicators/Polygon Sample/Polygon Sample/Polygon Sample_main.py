import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PolygonSample():
    def initialize(self):
        polygon = Polygon()
        polygon.FillColor = Color.Red
        polygon.Width = 200
        polygon.Height = 100
        polygon.Margin = Thickness(10)
        polygon.Points = [Point(100, 100), Point(200, 50), Point(300, 100), Point(100, 100)]

        api.Chart.AddControl(polygon)