import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MarketHoursSample():
    def initialize(self):
        grid = Grid(6, 2)
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

        titleTextBlock = self.get_text_block("Symbol Info")
        titleTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        
        grid.AddChild(titleTextBlock, 0, 0, 1, 2);
        grid.AddChild(self.get_text_block("Time Till Open"), 1, 0)

        self.timeTillOpenTextBlock = self.get_text_block(str(self.symbol.MarketHours.TimeTillOpen()))

        grid.AddChild(self.timeTillOpenTextBlock, 1, 1)
        grid.AddChild(self.get_text_block("Time Till Close"), 2, 0)

        self.timeTillCloseTextBlock = self.get_text_block(str(self.symbol.MarketHours.TimeTillClose()))

        grid.AddChild(self.timeTillCloseTextBlock, 2, 1);

        grid.AddChild(self.get_text_block("Is Opened"), 3, 0)

        self.isOpenedTextBlock = self.get_text_block(str(self.symbol.MarketHours.IsOpened()))

        grid.AddChild(self.isOpenedTextBlock, 3, 1)

        grid.AddChild(self.get_text_block("Trading Sessions #"), 4, 0)
        grid.AddChild(self.get_text_block(str(self.symbol.MarketHours.Sessions.Count)), 4, 1)

        grid.AddChild(self.get_text_block("Trading Session Week Days"), 5, 0)

        weekDays = ""

        for session in range(self.symbol.MarketHours.Sessions.Count):
            currentSessionWeekDays = f"{self.symbol.MarketHours.Sessions[session].StartDay}({self.symbol.MarketHours.Sessions[session].StartTime})-{self.symbol.MarketHours.Sessions[session].EndDay}({self.symbol.MarketHours.Sessions[session].EndTime})"
            weekDays = currentSessionWeekDays if session == 0 else f"{weekDays}, {currentSessionWeekDays}"

        grid.AddChild(self.get_text_block(weekDays), 5, 1)

        api.Chart.AddControl(grid)
        api.Timer.Start(1)

    def on_timer(self):
        self.timeTillOpenTextBlock.Text = str(self.symbol.MarketHours.TimeTillOpen())
        self.timeTillCloseTextBlock.Text = str(self.symbol.MarketHours.TimeTillClose())
        self.isOpenedTextBlock.Text = str(self.symbol.MarketHours.IsOpened())

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock