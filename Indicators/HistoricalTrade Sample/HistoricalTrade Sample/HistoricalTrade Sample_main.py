import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class HistoricalTradeSample():
    def initialize(self):
        self.stackPanel = StackPanel()
        self.stackPanel.Orientation = Orientation.Vertical
        self.stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        self.stackPanel.VerticalAlignment = VerticalAlignment.Center
        self.stackPanel.BackgroundColor = Color.Gold

        self.textBlocksStyle = Style()
        self.textBlocksStyle.Set(ControlProperty.Margin, Thickness(5))
        
        textBlock = self.get_text_block("Your Last 10 Trades")
        textBlock.FontWeight = FontWeight.ExtraBold
        textBlock.HorizontalAlignment = HorizontalAlignment.Center

        self.stackPanel.AddChild(textBlock)

        api.Chart.AddControl(self.stackPanel)

        self.update_last_trades()

        api.Positions.Closed += lambda _: self.update_last_trades()

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.textBlocksStyle
        return textBlock

    def update_last_trades(self):
        if hasattr(self, "tradesGrid") and self.tradesGrid is not None:
            self.stackPanel.RemoveChild(self.tradesGrid)

        self.tradesGrid = Grid(11, 6)

        self.tradesGrid.AddChild(self.get_text_block("Symbol"), 0, 0)
        self.tradesGrid.AddChild(self.get_text_block("Direction"), 0, 1)
        self.tradesGrid.AddChild(self.get_text_block("Volume"), 0, 2)
        self.tradesGrid.AddChild(self.get_text_block("Open Time"), 0, 3)
        self.tradesGrid.AddChild(self.get_text_block("Close Time"), 0, 4)
        self.tradesGrid.AddChild(self.get_text_block("Net Profit"), 0, 5)

        lastTenTrades = sorted(api.History, key=lambda trade: trade.ClosingTime, reverse=True)[:10]

        for iRowIndex in range(1, len(lastTenTrades) + 1):
            trade = lastTenTrades[iRowIndex - 1]

            self.tradesGrid.AddChild(self.get_text_block(trade.SymbolName), iRowIndex, 0)
            self.tradesGrid.AddChild(self.get_text_block(str(trade.TradeType)), iRowIndex, 1)
            self.tradesGrid.AddChild(self.get_text_block(str(trade.VolumeInUnits)), iRowIndex, 2)
            self.tradesGrid.AddChild(self.get_text_block(trade.EntryTime.ToString("o")), iRowIndex, 3)
            self.tradesGrid.AddChild(self.get_text_block(trade.ClosingTime.ToString("o")), iRowIndex, 4)
            self.tradesGrid.AddChild(self.get_text_block(str(trade.NetProfit)), iRowIndex, 5)

        self.stackPanel.AddChild(self.tradesGrid)