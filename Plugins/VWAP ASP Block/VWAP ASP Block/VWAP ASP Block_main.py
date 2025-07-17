import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class VWAPASPBlock():
    def on_start(self):
        block = api.Asp.SymbolTab.AddBlock("VWAP ASP Block");
        block.Height = 100;
            
        panel = StackPanel()
        panel.Orientation = Orientation.Vertical
            
        textBoxStyle = Style()
        textBoxStyle.Set(ControlProperty.Width, 200);
        textBoxStyle.Set(ControlProperty.Margin, Thickness(5));
        textBoxStyle.Set(ControlProperty.FontFamily, "Cambria");
        textBoxStyle.Set(ControlProperty.FontSize, 15);
            
        txtBuyVWAP = TextBlock()
        txtBuyVWAP.Text = "Buy Text Block"
        txtBuyVWAP.Style = textBoxStyle
        txtBuyVWAP.ForegroundColor = Color.Green
            
        txtSellVWAP = TextBlock()
        txtSellVWAP.Text = "Sell Text Block"
        txtSellVWAP.Style = textBoxStyle
        txtSellVWAP.ForegroundColor = Color.Red
            
        panel.AddChild(txtBuyVWAP);
        panel.AddChild(txtSellVWAP);
            
        block.Child = panel
            
        buyPositions = [pos for pos in api.Positions if pos.TradeType == TradeType.Buy]
        buyVwap = round(sum([p.EntryPrice * p.VolumeInUnits for p in buyPositions]) / sum([p.VolumeInUnits for p in buyPositions]), 5) if len(buyPositions) > 0 else 0
        txtBuyVWAP.Text = f"Buy Positions VWAP: {buyVwap}"

        sellPositions = [pos for pos in api.Positions if pos.TradeType == TradeType.Sell]
        sellVwap = round(sum([p.EntryPrice * p.VolumeInUnits for p in sellPositions]) / sum([p.VolumeInUnits for p in sellPositions]), 5) if len(sellPositions) > 0 else 0
        txtSellVWAP.Text = f"Sell Positions VWAP: {sellVwap}"
