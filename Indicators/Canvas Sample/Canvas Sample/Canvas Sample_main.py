import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CanvasSample():
    def initialize(self):
        canvas = Canvas()
        canvas.HorizontalAlignment = HorizontalAlignment.Center
        canvas.VerticalAlignment = VerticalAlignment.Center
        canvas.Width = 300
        canvas.Height = 200
        canvas.BackgroundColor = Color.Red
        canvas.Opacity = 0.5

        button = Button()
        button.Top = 20
        button.Left = 80
        button.Margin = Thickness(5)
        button.Text = "Button Inside Canvas"

        canvas.AddChild(button)

        svgImage = Image()
        svgImage.Source = SvgIcon(api.Svg)
        svgImage.Margin = Thickness(5)
        svgImage.Width = 128
        svgImage.Height = 128
        svgImage.Top = 45
        svgImage.Left = 80

        canvas.AddChild(svgImage)

        api.Chart.AddControl(canvas);