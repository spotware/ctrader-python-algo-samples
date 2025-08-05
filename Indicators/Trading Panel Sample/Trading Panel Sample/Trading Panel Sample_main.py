import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class TradingPanelSample():
    def initialize(self):
        tradeButtonBuy = Button()
        tradeButtonBuy.Text = "Buy"
        tradeButtonBuy.ForegroundColor = Color.White
        tradeButtonBuy.BackgroundColor = Color.Green
        tradeButtonBuy.Height = 25
        tradeButtonBuy.Width = 75
        tradeButtonBuy.Margin = Thickness(2)

        tradeButtonBuy.Click += lambda _: api.ExecuteMarketOrderAsync(TradeType.Buy, api.SymbolName, api.Symbol.VolumeInUnitsMin)

        tradeButtonSell = Button()
        tradeButtonSell.Text = "Sell"
        tradeButtonSell.ForegroundColor = Color.White
        tradeButtonSell.BackgroundColor = Color.Green
        tradeButtonSell.Height = 25
        tradeButtonSell.Width = 75
        tradeButtonSell.Margin = Thickness(2)

        tradeButtonSell.Click += lambda _: api.ExecuteMarketOrderAsync(TradeType.Sell, api.SymbolName, api.Symbol.VolumeInUnitsMin)

        grid = Grid(1, 2)
        
        grid.AddChild(tradeButtonBuy, 0,0)
        grid.AddChild(tradeButtonSell, 0, 1)
        
        api.Chart.AddControl(grid)