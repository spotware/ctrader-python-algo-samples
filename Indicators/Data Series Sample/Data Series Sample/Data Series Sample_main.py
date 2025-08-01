import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class DataSeriesSample():
    def initialize(self):
        grid = Grid(3, 2)
        grid.BackgroundColor = Color.DarkGoldenrod
        grid.HorizontalAlignment = HorizontalAlignment.Left
        grid.VerticalAlignment = VerticalAlignment.Bottom
        grid.Opacity = 0.5

        grid.AddChild(self.get_text_block("Last Value"), 0, 0)

        self.lastValueTextBlock = self.get_text_block(str(api.Source.LastValue))

        grid.AddChild(self.lastValueTextBlock, 0, 1)
        grid.AddChild(self.get_text_block("Last Closed Value"), 1, 0)

        self.lastClosedValueTextBlock = self.get_text_block(str(api.Source.Last(1)))

        grid.AddChild(self.lastClosedValueTextBlock, 1, 1)

        grid.AddChild(self.get_text_block("Values Count"), 2, 0)

        self.countTextBlock = self.get_text_block(str(api.Source.Count))

        grid.AddChild(self.countTextBlock, 2, 1)

        api.Chart.AddControl(grid)

    def calculate(self, index):
        # You can also use "LastValue" property if you don't have index
        self.lastValueTextBlock.Text = str(api.Source[index])
        # You can also use "Last(1)" property if you don't have index
        self.lastClosedValueTextBlock.Text = str(api.Source[index - 1])
        self.countTextBlock.Text = str(api.Source.Count)

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Margin = Thickness(5)
        return textBlock