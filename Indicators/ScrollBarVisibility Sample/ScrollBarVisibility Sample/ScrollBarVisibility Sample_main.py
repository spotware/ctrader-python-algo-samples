import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ScrollBarVisibilitySample():
    def initialize(self):
        scrollViewer = ScrollViewer()
        scrollViewer.HorizontalAlignment = HorizontalAlignment.Center
        scrollViewer.VerticalAlignment = VerticalAlignment.Center
        scrollViewer.BackgroundColor = Color.Gold
        scrollViewer.Opacity = 0.7
        scrollViewer.HorizontalScrollBarVisibility = api.HorizontalScrollBarVisibility
        scrollViewer.VerticalScrollBarVisibility = api.VerticalScrollBarVisibility
        scrollViewer.Height = 100

        grid = Grid(10, 2)
        grid.BackgroundColor = Color.Gold
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center

        scrollViewer.Content = grid

        for iRow in range(10):
            textBlock = TextBlock()
            textBlock.Text = "Text"
            textBlock.Margin = Thickness(5)
            textBlock.ForegroundColor = Color.Black
            textBlock.FontWeight = FontWeight.ExtraBold

            grid.AddChild(textBlock, iRow, 0)

            button = Button()
            button.Text = "Button"
            button.Margin = Thickness(5)
            button.ForegroundColor = Color.Black
            button.FontWeight = FontWeight.ExtraBold

            grid.AddChild(button, iRow, 1)

        api.Chart.AddControl(scrollViewer)