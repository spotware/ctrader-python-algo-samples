import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class EllipseShapeSample():
    def initialize(self):
        ellipse = Ellipse()
        ellipse.HorizontalAlignment = HorizontalAlignment.Center
        ellipse.VerticalAlignment = VerticalAlignment.Center
        ellipse.Margin = Thickness(5)
        ellipse.Width = 100
        ellipse.Height = 200
        ellipse.StrokeColor = Color.Black
        ellipse.FillColor = Color.Aqua
        ellipse.StrokeThickness = 2
        ellipse.StrokeStartLineCap = PenLineCap.Square
        ellipse.Left = 100
        ellipse.Top = 50

        canvas = Canvas()
        canvas.BackgroundColor = Color.Gold
        canvas.Opacity = 0.5

        canvas.AddChild(ellipse)

        api.Chart.AddControl(canvas)