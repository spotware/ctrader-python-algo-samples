import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class GridColumnSample():
    def initialize(self):
        grid = Grid(5, api.GridColumnsNumber)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center
        grid.ShowGridLines = True

        for iRow in range(5):
            row = grid.Rows[iRow]
            for iColumn in range(api.GridColumnsNumber):
                column = grid.Columns[iColumn]
                self.set_grid_column_length(column)

                textBlock = TextBlock()
                textBlock.Text = f"Row {iRow} and Column {iColumn}"
                textBlock.Margin = Thickness(5)
                textBlock.ForegroundColor = Color.Black
                textBlock.FontWeight = FontWeight.ExtraBold

                grid.AddChild(textBlock, iRow, iColumn)

        api.Chart.AddControl(grid)

    def set_grid_column_length(self, column):
        match api.GridColumnLengthUnitType:
            case GridUnitType.Auto:
                column.SetWidthToAuto()
            case GridUnitType.Pixel:
                column.SetWidthInPixels(api.GridColumnLength)
            case GridUnitType.Star:
                column.SetWidthInStars(api.GridColumnLength)