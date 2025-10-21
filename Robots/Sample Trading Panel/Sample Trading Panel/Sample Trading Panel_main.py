import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SampleTradingPanel():
    def on_start(self):
        tradingPanel = TradingPanel()

        border = Border()
        border.VerticalAlignment = api.PanelVerticalAlignment
        border.HorizontalAlignment = api.PanelHorizontalAlignment
        border.Style = Styles.create_panel_background_Style()
        border.Margin = Thickness(20, 40, 20, 20)
        border.Width = 225
        border.Child = tradingPanel.child

        api.Chart.AddControl(border)

class TradingPanel():
    LotsInputKey = "LotsKey";
    TakeProfitInputKey = "TPKey";
    StopLossInputKey = "SLKey";

    def __init__(self):
        self.inputMap = {}
        self.child = self.create_trading_panel(api.DefaultLots, api.DefaultStopLossPips, api.DefaultTakeProfitPips)

    def create_trading_panel(self, defaultLots, defaultStopLossPips, defaultTakeProfitPips):
        mainPanel = StackPanel()

        header = self.create_header()
        
        mainPanel.AddChild(header)

        contentPanel = self.create_content_panel(defaultLots, defaultStopLossPips, defaultTakeProfitPips)
        
        mainPanel.AddChild(contentPanel)

        return mainPanel

    def create_header(self):
        headerBorder = Border() 
        headerBorder.BorderThickness = Thickness(0, 0, 0, 1)
        headerBorder.Style = Styles.create_common_border_style()

        header = TextBlock()
        header.Text = "Quick Trading Panel"
        header.Margin = Thickness(10, 7, 10, 7)
        header.Style = Styles.create_header_style()

        headerBorder.Child = header
        return headerBorder

    def create_content_panel(self, defaultLots, defaultStopLossPips, defaultTakeProfitPips):
        contentPanel = StackPanel()
        contentPanel.Margin = Thickness(10)

        grid = Grid(4, 3)
        grid.Columns[1].SetWidthInPixels(5)

        sellButton = self.create_trade_button("SELL", Styles.create_sell_button_style(), TradeType.Sell)
        grid.AddChild(sellButton, 0, 0)

        buyButton = self.create_trade_button("BUY", Styles.create_buy_button_style(), TradeType.Buy)
        grid.AddChild(buyButton, 0, 2)

        lotsInput = self.create_input_with_label("Quantity (Lots)", str(defaultLots), self.LotsInputKey)
        grid.AddChild(lotsInput, 1, 0, 1, 3)

        stopLossInput = self.create_input_with_label("Stop Loss (Pips)", str(defaultStopLossPips), self.StopLossInputKey)
        grid.AddChild(stopLossInput, 2, 0)

        takeProfitInput = self.create_input_with_label("Take Profit (Pips)", str(defaultTakeProfitPips), self.TakeProfitInputKey)
        grid.AddChild(takeProfitInput, 2, 2)

        closeAllButton = self.create_close_all_button()
        grid.AddChild(closeAllButton, 3, 0, 1, 3);

        contentPanel.AddChild(grid)

        return contentPanel

    def create_trade_button(self, text, style, tradeType):
        tradeButton = Button() 
        tradeButton.Text = text
        tradeButton.Style = style
        tradeButton.Height = 25

        tradeButton.Click += lambda _ : self.execute_market_order_async(tradeType)

        return tradeButton

    def create_close_all_button(self):
        closeAllBorder = Border()
        closeAllBorder.Margin = Thickness(0, 10, 0, 0)
        closeAllBorder.BorderThickness = Thickness(0, 1, 0, 0)
        closeAllBorder.Style = Styles.create_common_border_style()

        closeButton = Button()
        closeButton.Style = Styles.create_close_button_style()
        closeButton.Text = "Close All"
        closeButton.Margin = Thickness(0, 10, 0, 0)

        closeButton.Click += lambda _ : self.close_all()

        closeAllBorder.Child = closeButton

        return closeAllBorder

    def create_input_with_label(self, label, defaultValue, inputKey):
        stackPanel = StackPanel()
        stackPanel.Orientation = Orientation.Vertical
        stackPanel.Margin = Thickness(0, 10, 0, 0)

        textBlock = TextBlock()
        textBlock.Text = label

        textBox = TextBox()
        textBox.Margin = Thickness(0, 5, 0, 0)
        textBox.Text = defaultValue
        textBox.Style = Styles.create_input_style()

        self.inputMap[inputKey] = textBox

        stackPanel.AddChild(textBlock)
        stackPanel.AddChild(textBox)

        return stackPanel

    def execute_market_order_async(self, tradeType):
        lots = self.get_value_from_input(self.LotsInputKey, 0)

        if lots <= 0:
            api.Print(f"{tradeType} failed, invalid Lots")
            return

        stopLossPips = self.get_value_from_input(self.StopLossInputKey, 0)
        takeProfitPips = self.get_value_from_input(self.TakeProfitInputKey, 0)

        api.Print(f"Open position with: LotsParameter: {lots}, StopLossPipsParameter: {stopLossPips}, TakeProfitPipsParameter: {takeProfitPips}")

        volume = api.Symbol.QuantityToVolumeInUnits(lots)

        api.ExecuteMarketOrderAsync(tradeType, api.Symbol.Name, volume, "Trade Panel Sample", stopLossPips, takeProfitPips)

    def get_value_from_input(self, inputKey, defaultValue):
        return float(self.inputMap[inputKey].Text)

    def close_all(self):
        for position in api.Positions:
            api.ClosePositionAsync(position)

class Styles():
    def create_panel_background_Style():
        style = Style()
        style.Set(ControlProperty.CornerRadius, 3)
        style.Set(ControlProperty.BackgroundColor, Styles.get_color_with_opacity(Color.FromHex("#292929"), 0.85), ControlState.DarkTheme)
        style.Set(ControlProperty.BackgroundColor, Styles.get_color_with_opacity(Color.FromHex("#FFFFFF"), 0.85), ControlState.LightTheme)
        style.Set(ControlProperty.BorderColor, Color.FromHex("#3C3C3C"), ControlState.DarkTheme)
        style.Set(ControlProperty.BorderColor, Color.FromHex("#C3C3C3"), ControlState.LightTheme)
        style.Set(ControlProperty.BorderThickness, Thickness(1))

        return style

    def create_common_border_style():
        style = Style()
        style.Set(ControlProperty.BorderColor, Styles.get_color_with_opacity(Color.FromHex("#FFFFFF"), 0.12), ControlState.DarkTheme);
        style.Set(ControlProperty.BorderColor, Styles.get_color_with_opacity(Color.FromHex("#000000"), 0.12), ControlState.LightTheme)
        return style

    def create_header_style():
        style = Style()
        style.Set(ControlProperty.ForegroundColor, Styles.get_color_with_opacity(Color.FromHex("#FFFFFF"), 0.70), ControlState.DarkTheme)
        style.Set(ControlProperty.ForegroundColor, Styles.get_color_with_opacity(Color.FromHex("#000000"), 0.65), ControlState.LightTheme)
        return style;

    def create_input_style():
        style = Style(DefaultStyles.TextBoxStyle)
        style.Set(ControlProperty.BackgroundColor, Color.FromHex("#1A1A1A"), ControlState.DarkTheme)
        style.Set(ControlProperty.BackgroundColor, Color.FromHex("#111111"), ControlState.DarkTheme | ControlState.Hover)
        style.Set(ControlProperty.BackgroundColor, Color.FromHex("#E7EBED"), ControlState.LightTheme)
        style.Set(ControlProperty.BackgroundColor, Color.FromHex("#D6DADC"), ControlState.LightTheme | ControlState.Hover)
        style.Set(ControlProperty.CornerRadius, 3)
        return style

    def create_buy_button_style():
        return Styles.create_button_style(Color.FromHex("#009345"), Color.FromHex("#10A651"))

    def create_sell_button_style():
        return Styles.create_button_style(Color.FromHex("#F05824"), Color.FromHex("#FF6C36"))

    def create_close_button_style():
        return Styles.create_button_style(Color.FromHex("#F05824"), Color.FromHex("#FF6C36"))

    def create_button_style(color, hoverColor):
        style = Style(DefaultStyles.ButtonStyle)
        style.Set(ControlProperty.BackgroundColor, color, ControlState.DarkTheme);
        style.Set(ControlProperty.BackgroundColor, color, ControlState.LightTheme);
        style.Set(ControlProperty.BackgroundColor, hoverColor, ControlState.DarkTheme | ControlState.Hover);
        style.Set(ControlProperty.BackgroundColor, hoverColor, ControlState.LightTheme | ControlState.Hover);
        style.Set(ControlProperty.ForegroundColor, Color.FromHex("#FFFFFF"), ControlState.DarkTheme);
        style.Set(ControlProperty.ForegroundColor, Color.FromHex("#FFFFFF"), ControlState.LightTheme);
        return style

    def get_color_with_opacity(baseColor, opacity):
        alpha = round(255 * opacity)
        return Color.FromArgb(alpha, baseColor)
