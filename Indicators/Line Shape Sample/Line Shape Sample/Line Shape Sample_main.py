import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LineShapeSample():
    def initialize(self):
        xCenter = api.Chart.Width / 2
        yCenter = api.Chart.Height / 2

        line = Line()
        line.X1 = xCenter
        line.X2 = xCenter + 100
        line.Y1 = yCenter
        line.Y2 = yCenter + 100
        line.StrokeColor = Color.Red
        line.StrokeThickness = 2

        api.Chart.AddControl(line)