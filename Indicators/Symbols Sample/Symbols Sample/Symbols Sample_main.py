import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SymbolsSample():
    def initialize(self):
        scrollViewer = ScrollViewer()
        scrollViewer.HorizontalAlignment = HorizontalAlignment.Center
        scrollViewer.VerticalAlignment = VerticalAlignment.Center
        scrollViewer.BackgroundColor = Color.Gold
        scrollViewer.Opacity = 0.7
        scrollViewer.HorizontalScrollBarVisibility = ScrollBarVisibility.Auto
        scrollViewer.VerticalScrollBarVisibility = ScrollBarVisibility.Visible
        scrollViewer.Height = 300

        grid = Grid(api.Symbols.Count, 2)
        grid.BackgroundColor = Color.Gold
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center

        scrollViewer.Content = grid

        for iSymbol in range(api.Symbols.Count):
            symbolName = api.Symbols[iSymbol]
            symbol = api.Symbols.GetSymbol(symbolName)

            if symbol.MarketHours.IsOpened() == False:
                continue

            symbolNameTextBlock = TextBlock()
            symbolNameTextBlock.Text = symbolName
            symbolNameTextBlock.Margin = Thickness(5)
            symbolNameTextBlock.ForegroundColor = Color.Black
            symbolNameTextBlock.FontWeight = FontWeight.ExtraBold

            grid.AddChild(symbolNameTextBlock, iSymbol, 0)

            symbolDescriptionTextBlock = TextBlock()
            symbolDescriptionTextBlock.Text = symbol.Description
            symbolDescriptionTextBlock.Margin = Thickness(5)
            symbolDescriptionTextBlock.ForegroundColor = Color.Black
            symbolDescriptionTextBlock.FontWeight = FontWeight.ExtraBold

            grid.AddChild(symbolDescriptionTextBlock, iSymbol, 1);

        api.Chart.AddControl(scrollViewer);