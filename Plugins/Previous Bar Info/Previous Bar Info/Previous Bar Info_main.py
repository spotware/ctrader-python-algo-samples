import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class PreviousBarInfo():
    def on_start(self):
        tradeWatchTab = api.TradeWatch.AddTab("Previous Bar Info")
        tradeWatchTab.IsSelected = True
            
        webView = WebView()              
        tradeWatchTab.Child = webView
            
        webView.NavigateAsync("https://ctrader.com/")
            
        grid = Grid(2, 2) 
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center
        grid.ShowGridLines = True
        grid.Height = 150
        grid.Width = 150
            
        self.bars = api.MarketData.GetBars(TimeFrame.Minute, "USDJPY")
            
        self.lowBlock = self.get_text_block(f"Low: {self.bars.LowPrices.LastValue}")
        self.highBlock = self.get_text_block(f"High: {self.bars.HighPrices.LastValue}")
        self.openBlock = self.get_text_block(f"Open: {self.bars.OpenPrices.LastValue}")
        self.closeBlock = self.get_text_block(f"Close: {self.bars.ClosePrices.LastValue}")
            
        grid.AddChild(self.lowBlock, 0, 0)
        grid.AddChild(self.highBlock, 0, 1)
        grid.AddChild(self.openBlock, 1, 0)
        grid.AddChild(self.closeBlock, 1, 1)

        tradeWatchTab.Child = grid
            
        self.bars.Tick += self.on_bars_Tick
    
    def on_bars_Tick(self, args):
        self.lowBlock.Text = f"Low: {self.bars.LowPrices.LastValue}"
        self.highBlock.Text = f"High: {self.bars.HighPrices.LastValue}"
        self.openBlock.Text = f"Open: {self.bars.OpenPrices.LastValue}"
        self.closeBlock.Text = f"Close: {self.bars.ClosePrices.LastValue}"

    def get_text_block(self, text):
        textblock = TextBlock()
        textblock.Text = text
        textblock.HorizontalAlignment = HorizontalAlignment.Center
        textblock.VerticalAlignment = VerticalAlignment.Center
        return textblock