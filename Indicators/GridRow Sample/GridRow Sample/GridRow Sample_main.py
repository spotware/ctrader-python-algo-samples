import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class GridRowSample():
    def initialize(self):
        grid = Grid(api.GridRowsNumber, 2)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center
        grid.ShowGridLines = True

        for iRow in range(api.GridRowsNumber):
            row = grid.Rows[iRow]
            self.set_grid_row_length(row)

            for iColumn in range(2):
                column = grid.Columns[iColumn]

                textBlock = TextBlock()
                textBlock.Text = f"Row {iRow} and Column {iColumn}"
                textBlock.Margin = Thickness(5)
                textBlock.ForegroundColor = Color.Black
                textBlock.FontWeight = FontWeight.ExtraBold

                grid.AddChild(textBlock, iRow, iColumn)

        api.Chart.AddControl(grid)

    def set_grid_row_length(self, row):
        match api.GridRowLengthUnitType:
            case GridUnitType.Auto:
                row.SetHeightToAuto()
            case GridUnitType.Pixel:
                row.SetHeightInPixels(api.GridRowLength)
            case GridUnitType.Star:
                row.SetHeightInStars(api.GridRowLength)