import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class FillRuleSample():
    def initialize(self):
        stackPanelNonzero = StackPanel()
        stackPanelNonzero.HorizontalAlignment = HorizontalAlignment.Center
        stackPanelNonzero.VerticalAlignment = VerticalAlignment.Center
        stackPanelNonzero.BackgroundColor = Color.Gold
        stackPanelNonzero.Opacity = 0.6

        nonZeroTextBlock = TextBlock()
        nonZeroTextBlock.Text = "Nonzero"
        nonZeroTextBlock.ForegroundColor = Color.Black
        nonZeroTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        nonZeroTextBlock.Margin = Thickness(10)

        stackPanelNonzero.AddChild(nonZeroTextBlock)

        nonzeroPolygon = Polygon()
        nonzeroPolygon.FillColor = Color.Red
        nonzeroPolygon.Width = 200
        nonzeroPolygon.Height = 100
        nonzeroPolygon.FillRule = FillRule.Nonzero
        nonzeroPolygon.Margin = Thickness(10)
        nonzeroPolygon.Points = [
            Point(1, 200),
            Point(50, 30),
            Point(100, 1),
            Point(150, 1),
            Point(100, 10),
            Point(50, 1),
            Point(200, 70),
            Point(300, 90)
        ]

        stackPanelNonzero.AddChild(nonzeroPolygon);

        evenOddTextBlock = TextBlock()
        evenOddTextBlock.Text = "EvenOdd"
        evenOddTextBlock.ForegroundColor = Color.Black
        evenOddTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        evenOddTextBlock.Margin = Thickness(10)

        stackPanelNonzero.AddChild(evenOddTextBlock)

        evenOddPolygon = Polygon()
        evenOddPolygon.FillColor = Color.Red
        evenOddPolygon.Width = 200
        evenOddPolygon.Height = 100
        evenOddPolygon.FillRule = FillRule.EvenOdd
        evenOddPolygon.Margin = Thickness(10)
        evenOddPolygon.Points = [
            Point(1, 200),
            Point(50, 30),
            Point(100, 1),
            Point(150, 1),
            Point(100, 10),
            Point(50, 1),
            Point(200, 70),
            Point(300, 90)
        ]

        stackPanelNonzero.AddChild(evenOddPolygon)

        api.Chart.AddControl(stackPanelNonzero)