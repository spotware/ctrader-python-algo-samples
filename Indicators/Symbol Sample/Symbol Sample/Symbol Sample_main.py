import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SymbolSample():
    def initialize(self):
        grid = Grid(24, 2)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center

        self.style = Style()

        self.style.Set(ControlProperty.Padding, 1)
        self.style.Set(ControlProperty.Margin, Thickness(2))
        self.style.Set(ControlProperty.BackgroundColor, Color.Black)
        self.style.Set(ControlProperty.FontSize, 8)

        self.symbol = api.Symbol if api.UseCurrentSymbol else api.Symbols.GetSymbol(api.OtherSymbolName)

        grid.AddChild(self.get_text_block("Symbol Info", HorizontalAlignment.Center), 0, 0, 1, 2)
        grid.AddChild(self.get_text_block("Name"), 1, 0)
        grid.AddChild(self.get_text_block(self.symbol.Name), 1, 1)
        grid.AddChild(self.get_text_block("ID"), 2, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.Id)), 2, 1)
        grid.AddChild(self.get_text_block("Digits"), 3, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.Digits)), 3, 1)
        grid.AddChild(self.get_text_block("Description"), 4, 0)
        grid.AddChild(self.get_text_block(self.symbol.Description), 4, 1)
        grid.AddChild(self.get_text_block("Lot Size"), 5, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.LotSize)), 5, 1)
        grid.AddChild(self.get_text_block("Pip Size"), 6, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.PipSize)), 6, 1)
        grid.AddChild(self.get_text_block("Pip Value"), 7, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.PipValue)), 7, 1)
        grid.AddChild(self.get_text_block("Tick Size"), 8, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.TickSize)), 8, 1)
        grid.AddChild(self.get_text_block("Tick Value"), 9, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.TickValue)), 9, 1)
        grid.AddChild(self.get_text_block("Volume In Units Max"), 10, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.VolumeInUnitsMax)), 10, 1)
        grid.AddChild(self.get_text_block("Volume In Units Min"), 11, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.VolumeInUnitsMin)), 11, 1)
        grid.AddChild(self.get_text_block("Volume In Units Step"), 12, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.VolumeInUnitsStep)), 12, 1)
        grid.AddChild(self.get_text_block("Ask"), 13, 0)

        self.askTextBlock = self.get_text_block(str(self.symbol.Ask))

        grid.AddChild(self.askTextBlock, 13, 1)

        grid.AddChild(self.get_text_block("Bid"), 14, 0)

        self.bidTextBlock = self.get_text_block(str(self.symbol.Bid))

        grid.AddChild(self.bidTextBlock, 14, 1)

        grid.AddChild(self.get_text_block("Spread"), 15, 0)

        self.spreadTextBlock = self.get_text_block(str(self.symbol.Spread))

        grid.AddChild(self.spreadTextBlock, 15, 1)

        grid.AddChild(self.get_text_block("Unrealized Gross Profit"), 16, 0)

        self.unrealizedGrossProfitTextBlock = self.get_text_block(str(self.symbol.UnrealizedGrossProfit))

        grid.AddChild(self.unrealizedGrossProfitTextBlock, 16, 1)

        grid.AddChild(self.get_text_block("Unrealized Net Profit"), 17, 0)

        self.unrealizedNetProfitTextBlock = self.get_text_block(str(self.symbol.UnrealizedNetProfit))

        grid.AddChild(self.unrealizedNetProfitTextBlock, 17, 1)

        grid.AddChild(self.get_text_block("Time Till Open"), 18, 0)

        self.timeTillOpenTextBlock = self.get_text_block(str(self.symbol.MarketHours.TimeTillOpen()))

        grid.AddChild(self.timeTillOpenTextBlock, 18, 1)

        grid.AddChild(self.get_text_block("Time Till Close"), 19, 0)

        self.timeTillCloseTextBlock = self.get_text_block(str(self.symbol.MarketHours.TimeTillClose()))

        grid.AddChild(self.timeTillCloseTextBlock, 19, 1)

        grid.AddChild(self.get_text_block("Is Opened"), 20, 0)

        self.isOpenedTextBlock = self.get_text_block(str(self.symbol.MarketHours.IsOpened()))

        grid.AddChild(self.isOpenedTextBlock, 20, 1)

        grid.AddChild(self.get_text_block("Trading Sessions #"), 21, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.MarketHours.Sessions.Count)), 21, 1)

        grid.AddChild(self.get_text_block("Trading Session Week Days"), 22, 0)

        weekDays = ""

        for iSession in range(self.symbol.MarketHours.Sessions.Count):
            currentSessionWeekDays = f"{self.symbol.MarketHours.Sessions[iSession].StartDay}({self.symbol.MarketHours.Sessions[iSession].StartTime})-{self.symbol.MarketHours.Sessions[iSession].EndDay}({self.symbol.MarketHours.Sessions[iSession].EndTime})"
            weekDays = currentSessionWeekDays if iSession == 0 else f"{weekDays}, {currentSessionWeekDays}"

        grid.AddChild(self.get_text_block(weekDays), 22, 1)

        grid.AddChild(self.get_text_block("Leverage Tier"), 23, 0)

        leverageTiers = ""

        for iLeveragTier in range(self.symbol.DynamicLeverage.Count):
            currentLeverageTiers = f"Volume up to {self.symbol.DynamicLeverage[iLeveragTier].Volume} is {self.symbol.DynamicLeverage[iLeveragTier].Leverage}"
            leverageTiers = currentLeverageTiers if iLeveragTier == 0 else f"{leverageTiers}, {currentLeverageTiers}"

        grid.AddChild(self.get_text_block(leverageTiers), 23, 1)

        api.Chart.AddControl(grid)

        self.symbol.Tick += self.on_symbol_tick

        api.Timer.Start(1)
        
    def on_symbol_tick(self, args):
        self.askTextBlock.Text = str(args.Symbol.Ask)
        self.bidTextBlock.Text = str(args.Symbol.Bid)
        self.spreadTextBlock.Text = str(args.Symbol.Spread)
        self.unrealizedGrossProfitTextBlock.Text = str(args.Symbol.UnrealizedGrossProfit)
        self.unrealizedNetProfitTextBlock.Text = str(args.Symbol.UnrealizedNetProfit)

    def on_timer(self):
        self.timeTillOpenTextBlock.Text = str(self.symbol.MarketHours.TimeTillOpen())
        self.timeTillCloseTextBlock.Text = str(self.symbol.MarketHours.TimeTillClose())
        self.isOpenedTextBlock.Text = str(self.symbol.MarketHours.IsOpened())

    def get_text_block(self, text, horizontalAlignment = None):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        if horizontalAlignment is not None:
            textBlock.HorizontalAlignment = horizontalAlignment
        return textBlock