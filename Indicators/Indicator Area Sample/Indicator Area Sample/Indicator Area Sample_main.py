import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class IndicatorAreaSample():
    def initialize(self):
        grid = Grid(1, 2)
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.7
        grid.Width = 200

        indicatorAreaCountLabelTextBlock = TextBlock()
        indicatorAreaCountLabelTextBlock.Text = "Indicator Area #"
        indicatorAreaCountLabelTextBlock.Margin = Thickness(5)
        indicatorAreaCountLabelTextBlock.FontWeight = FontWeight.ExtraBold
        indicatorAreaCountLabelTextBlock.ForegroundColor = Color.Black

        grid.AddChild(indicatorAreaCountLabelTextBlock, 0, 0)

        self.indicatorAreaNumberTextBlock = TextBlock()
        self.indicatorAreaNumberTextBlock.Margin = Thickness(5)
        self.indicatorAreaNumberTextBlock.FontWeight = FontWeight.ExtraBold
        self.indicatorAreaNumberTextBlock.ForegroundColor = Color.Black

        grid.AddChild(self.indicatorAreaNumberTextBlock, 0, 1)

        api.IndicatorArea.AddControl(grid)

        self.update_area_count()
        
        api.Chart.IndicatorAreaAdded += lambda _: self.update_area_count()
        api.Chart.IndicatorAreaRemoved += lambda _: self.update_area_count()

    def update_area_count(self):
        self.indicatorAreaNumberTextBlock.Text = str(api.Chart.IndicatorAreas.Count)