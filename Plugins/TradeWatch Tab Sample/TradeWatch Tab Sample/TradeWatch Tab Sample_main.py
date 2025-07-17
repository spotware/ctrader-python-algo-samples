import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TradeWatchTabSample():
    def on_start(self):
        tab = api.TradeWatch.AddTab("Active Chart Symbol Stats")

        panel = StackPanel()
        panel.Orientation = Orientation.Vertical
        panel.HorizontalAlignment = HorizontalAlignment.Center

        self.symbolStatsControl = SymbolStatsControl()
        self.symbolStatsControl.Margin = Thickness(10)
        self.tradeControl = TradeControl(self.on_trade)
        self.tradeControl.Margin = Thickness(10)

        panel.AddChild(self.symbolStatsControl.content)
        panel.AddChild(self.tradeControl.content)

        tab.Child = panel

        self.set_symbol_stats()

        api.ChartManager.ActiveFrameChanged += lambda _ : self.set_symbol_stats()

    def on_trade(self, args):
        api.ExecuteMarketOrder(args["tradeType"], args["symbolName"], args["volume"])

    def set_symbol_stats(self):
        if api.ChartManager.ActiveFrame is None or isinstance(api.ChartManager.ActiveFrame.__implementation__, ChartFrame) == False:
            return;

        chartFrame = ChartFrame(api.ChartManager.ActiveFrame)
        self.tradeControl.set_symbol(chartFrame.Symbol)
        self.symbolStatsControl.set_symbol(chartFrame.Symbol)
    

class SymbolStatsControl():
    def __init__(self):
        self.__symbol__ = None
        self.content = StackPanel()
        self.content.Orientation = Orientation.Vertical

        self.symbolNameTextBlock = self.get_text_block()
        self.symbolPriceTextBlock = self.get_text_block()

        self.content.AddChild(self.wrap_in_horizontal_panel(self.symbolNameTextBlock, self.symbolPriceTextBlock))

        grid = Grid(10, 2)

        self.spreadTextBlock = self.get_text_block()

        grid.AddChild(self.get_text_block("Spread"), 0, 0)
        grid.AddChild(self.spreadTextBlock, 0, 1)

        self.unrealizedNetProfitTextBlock = self.get_text_block()

        grid.AddChild(self.get_text_block("Unrealized Net Profit"), 1, 0)
        grid.AddChild(self.unrealizedNetProfitTextBlock, 1, 1)

        self.unrealizedGrossProfitTextBlock = self.get_text_block()

        grid.AddChild(self.get_text_block("Unrealized Gross Profit"), 2, 0)
        grid.AddChild(self.unrealizedGrossProfitTextBlock, 2, 1)

        self.commissionTextBlock = self.get_text_block()

        grid.AddChild(self.get_text_block("Commission"), 3, 0)
        grid.AddChild(self.commissionTextBlock, 3, 1)

        self.content.AddChild(grid);

    def get_text_block(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 20
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock

    def wrap_in_horizontal_panel(self, *args):
        panel = StackPanel()
        panel.Orientation = Orientation.Horizontal

        for control in args:
            if control.Margin == Thickness(0):
                control.Margin = 3
            panel.AddChild(control)

        return panel

    def get_symbol(self):
        return self.__symbol__
    
    def set_symbol(self, symbol):
        if symbol is None or symbol == self.__symbol__:
            return

        self.update(symbol)

    def update(self, newSymbol):
        previousSymbol = self.__symbol__;
        self.__symbol__ = newSymbol;

        self.symbolNameTextBlock.Text = f"{newSymbol.Name} ({newSymbol.Description})"
        self.symbolPriceTextBlock.Text = f"Bid: {newSymbol.Bid}, Ask: {newSymbol.Ask}"
        self.spreadTextBlock.Text = f"{self.get_spread_in_pips(newSymbol)} Pips"
        self.unrealizedNetProfitTextBlock.Text = str(newSymbol.UnrealizedNetProfit)
        self.unrealizedGrossProfitTextBlock.Text = str(newSymbol.UnrealizedGrossProfit)
        self.commissionTextBlock.Text = f"{newSymbol.Commission} {newSymbol.CommissionType}"

        if previousSymbol is not None: 
            previousSymbol.Tick -= self.on_symbol_tick

        newSymbol.Tick += self.on_symbol_tick

    def get_spread_in_pips(self, symbol):
        return (symbol.Spread * pow(10, symbol.Digits)) / (symbol.PipSize / symbol.TickSize);

    def on_symbol_tick(self, args):
        self.symbolPriceTextBlock.Text = f"Bid: {args.Bid}, Ask: {args.Ask}"
        self.spreadTextBlock.Text = f"{self.get_spread_in_pips(args.Symbol)} Pips"
        self.unrealizedNetProfitTextBlock.Text = str(args.Symbol.UnrealizedNetProfit)
        self.unrealizedGrossProfitTextBlock.Text = str(args.Symbol.UnrealizedGrossProfit)

class TradeControl():
    def __init__(self, on_trade):
        self.__symbol__ = None
        self.__on_trade__ = on_trade
        self.content = Grid(10, 2)

        self.volumeTextBox = TextBox()
        self.volumeTextBox.MinWidth = 200
        self.volumeTextBox.FontFamily = "Calibri"
        self.volumeTextBox.FontSize = 20
        self.volumeTextBox.FontWeight = FontWeight.Bold
        self.volumeTextBox.Margin = Thickness(3)

        self.content.AddChild(self.get_text_block("Volume"), 0, 0)
        self.content.AddChild(self.volumeTextBox, 0, 1);

        self.tradeTypeComboBox = ComboBox()
        self.tradeTypeComboBox.MinWidth = 200
        self.tradeTypeComboBox.FontFamily = "Calibri"
        self.tradeTypeComboBox.FontSize = 20
        self.tradeTypeComboBox.FontWeight = FontWeight.Bold
        self.tradeTypeComboBox.Margin = Thickness(3)

        self.tradeTypeComboBox.AddItem("Buy")
        self.tradeTypeComboBox.AddItem("Sell")

        self.tradeTypeComboBox.SelectedItem = "Buy"

        tradeTypeTextBlock = self.get_text_block("Trade Type")

        tradeTypeTextBlock.VerticalAlignment = VerticalAlignment.Center

        self.content.AddChild(tradeTypeTextBlock, 1, 0)
        self.content.AddChild(self.tradeTypeComboBox, 1, 1)

        executeButton = Button()
        executeButton.Text = "Execute"
        executeButton.FontFamily = "Calibri"
        executeButton.BackgroundColor = Color.Red

        executeButton.Click += self.on_execute_button_click

        self.content.AddChild(executeButton, 2, 0, 1, 2);

    def get_text_block(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 20
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock

    def get_symbol(self):
        return self.__symbol__
    
    def set_symbol(self, symbol):
        if symbol is None or symbol == self.__symbol__:
            return

        self.__symbol__ = symbol
        self.volumeTextBox.Text = str(self.__symbol__.VolumeInUnitsMin)

    def on_execute_button_click(self, args):
        if self.__symbol__ is None:
            return;
        
        volume = float(self.volumeTextBox.Text)
        tradeType = TradeType.Buy if self.tradeTypeComboBox.SelectedItem == "Buy" else TradeType.Sell

        self.__on_trade__({"volume": volume, "tradeType": tradeType, "symbolName": self.__symbol__.Name});