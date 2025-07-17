import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class OrderByMargin():
    def on_start(self):
        self.viewModel = view_model(self.on_view_model_changed)

        self.button_styles = button_styles()
        self.add_controls()

        api.Positions.Opened += lambda _: self.update_available_margin()
        api.Positions.Closed += lambda _: self.update_available_margin()
        api.Positions.Modified += lambda _: self.update_available_margin()
        api.Asp.SymbolTab.SymbolChanged += lambda _: self.set_maximum_margin()
        api.Account.Switched += lambda _: self.set_maximum_margin()

        self.update_available_margin();
        self.set_maximum_margin();
    
    def on_view_model_changed(self):
        self.availableMarginTextBlock.Text = f"{math.floor(self.viewModel.get_available_margin())} {api.Account.Asset.Name}"
        self.quantityToTradeTextBlock.Text = str(round(self.viewModel.get_quantity(), 2))
        self.tradeableMarginTextBox.Text = str(self.viewModel.get_trade_margin())

    def add_controls(self):
        block = api.Asp.SymbolTab.AddBlock("New Order by Margin")
        block.IsDetachable = False
        block.Height = 150

        rootStackPanel = StackPanel()
        rootStackPanel.Margin = Thickness(10)

        availableMarginStackPanel = StackPanel()
        availableMarginStackPanel.Orientation = Orientation.Horizontal

        availableMarginLabelTextBlock = TextBlock()
        availableMarginLabelTextBlock.Text = "Available Margin: "

        availableMarginStackPanel.AddChild(availableMarginLabelTextBlock)

        self.availableMarginTextBlock = TextBlock()

        availableMarginStackPanel.AddChild(self.availableMarginTextBlock)

        rootStackPanel.AddChild(availableMarginStackPanel)

        tradeMarginLabelTextBlock = TextBlock()
        tradeMarginLabelTextBlock.Text = "Margin to trade:"
        tradeMarginLabelTextBlock.Margin = Thickness(0, 10, 0, 0)

        rootStackPanel.AddChild(tradeMarginLabelTextBlock)

        tradeMarginGrid = Grid()
        tradeMarginGrid.Margin = Thickness(10)

        tradeMarginGrid.AddColumn().SetWidthInStars(1)
        tradeMarginGrid.AddColumn().SetWidthToAuto()
        tradeMarginGrid.AddColumn().SetWidthToAuto()
        tradeMarginGrid.AddColumn().SetWidthToAuto()

        self.tradeableMarginTextBox = TextBox()
        self.tradeableMarginTextBox.IsReadOnly = True
        self.tradeableMarginTextBox.TextAlignment = TextAlignment.Right

        tradeableMarginTextBoxStyle = Style()
        tradeableMarginTextBoxStyle.Set(ControlProperty.BackgroundColor, Color.FromArgb(26, 26, 26), ControlState.DarkTheme)
        tradeableMarginTextBoxStyle.Set(ControlProperty.ForegroundColor, Color.FromArgb(255, 255, 255), ControlState.DarkTheme)
        tradeableMarginTextBoxStyle.Set(ControlProperty.BackgroundColor, Color.FromArgb(231, 235, 237), ControlState.LightTheme)
        tradeableMarginTextBoxStyle.Set(ControlProperty.ForegroundColor, Color.FromArgb(55, 56, 57), ControlState.LightTheme)

        self.tradeableMarginTextBox.Style = tradeableMarginTextBoxStyle

        tradeMarginGrid.AddChild(self.tradeableMarginTextBox, 0, 0)

        decreaseMarginButton = Button()
        decreaseMarginButton.Text = "-"
        decreaseMarginButton.Margin = Thickness(5, 0, 5, 0)
        decreaseMarginButton.Click += self.on_decrease_margin_button_click
        
        tradeMarginGrid.AddChild(decreaseMarginButton, 0, 1)

        increaseMarginButton = Button()
        increaseMarginButton.Text = "+"
        increaseMarginButton.Click += self.on_increase_margin_button_click
        
        tradeMarginGrid.AddChild(increaseMarginButton, 0, 2)

        maxMarginButton = Button()
        maxMarginButton.Text = "max"
        maxMarginButton.Margin = Thickness(5, 0, 0, 0)
        maxMarginButton.VerticalAlignment = VerticalAlignment.Stretch
        maxMarginButton.Click += self.on_max_margin_button_click
        
        tradeMarginGrid.AddChild(maxMarginButton, 0, 3)

        rootStackPanel.AddChild(tradeMarginGrid)

        volumeStackPanel = StackPanel()
        volumeStackPanel.Orientation = Orientation.Horizontal
        volumeStackPanel.HorizontalAlignment = HorizontalAlignment.Center

        quantityToTradeLabelTextBlock = TextBlock()
        quantityToTradeLabelTextBlock.Text = "Quantity to trade: "

        volumeStackPanel.AddChild(quantityToTradeLabelTextBlock)

        self.quantityToTradeTextBlock = TextBlock()

        volumeStackPanel.AddChild(self.quantityToTradeTextBlock);

        lotsLabelTextBlock = TextBlock()
        lotsLabelTextBlock.Text = "Lots"

        volumeStackPanel.AddChild(lotsLabelTextBlock)

        rootStackPanel.AddChild(volumeStackPanel)

        tradeButtons = StackPanel()
        tradeButtons.Orientation = Orientation.Horizontal
        tradeButtons.Margin = Thickness(10)
        tradeButtons.HorizontalAlignment = HorizontalAlignment.Center

        tradeButtons.AddChild(self.create_trade_button("Sell", self.button_styles.create_sell_button_style(), TradeType.Sell))
        tradeButtons.AddChild(self.create_trade_button("Buy", self.button_styles.create_buy_button_style(), TradeType.Buy))
        rootStackPanel.AddChild(tradeButtons)

        block.Child = rootStackPanel

    def create_trade_button(self, text, style, tradeType):
        tradeButton = Button()
        tradeButton.Text = text
        tradeButton.Style = style
        tradeButton.Height = 25

        tradeButton.Click += lambda _ : api.ExecuteMarketOrderAsync(tradeType, api.Asp.SymbolTab.Symbol.Name, self.viewModel.get_quantity() * api.Asp.SymbolTab.Symbol.LotSize)

        return tradeButton

    def on_decrease_margin_button_click(self, args):
        symbol = api.Asp.SymbolTab.Symbol;
        leverage = min(symbol.DynamicLeverage[0].Leverage, api.Account.PreciseLeverage);

        if self.viewModel.get_quantity() <= symbol.VolumeInUnitsMin  / symbol.LotSize:
            return;

        self.viewModel.set_quantity(self.viewModel.get_quantity() - (symbol.VolumeInUnitsMin / symbol.LotSize))
        self.recalculate_margin(self.viewModel.get_quantity())

    def on_increase_margin_button_click(self, args):
        symbol = api.Asp.SymbolTab.Symbol;
        leverage = min(symbol.DynamicLeverage[0].Leverage, api.Account.PreciseLeverage);

        if self.viewModel.get_quantity() > symbol.VolumeInUnitsMax / symbol.LotSize:
            return;

        self.viewModel.set_quantity(self.viewModel.get_quantity() + (symbol.VolumeInUnitsMin / symbol.LotSize))
        self.recalculate_margin(self.viewModel.get_quantity())

    def on_max_margin_button_click(self, args):
        self.set_maximum_margin()

    def set_maximum_margin(self):
        symbol = api.Asp.SymbolTab.Symbol;
        leverage = min(symbol.DynamicLeverage[0].Leverage, api.Account.PreciseLeverage);
        volume = api.Account.Asset.Convert(symbol.BaseAsset, api.Account.FreeMargin * leverage);
        tradeableVolume = symbol.NormalizeVolumeInUnits(volume, RoundingMode.Down);

        self.viewModel.set_quantity(tradeableVolume / symbol.LotSize)
        self.viewModel.set_trade_margin(symbol.BaseAsset.Convert(api.Account.Asset, tradeableVolume / leverage))

    def update_available_margin(self):
        self.viewModel.set_available_margin(api.Account.FreeMargin)

    def recalculate_margin(self, quantity):
        symbol = api.Asp.SymbolTab.Symbol
        leverage = min(symbol.DynamicLeverage[0].Leverage, api.Account.PreciseLeverage)
        volume = quantity * symbol.LotSize
        margin = symbol.BaseAsset.Convert(api.Account.Asset, volume / leverage)
        self.viewModel.set_trade_margin(math.floor(margin))

class view_model():
    def __init__(self, on_changed):
        self.__on_changed__ = on_changed
        self.__available_margin__ = 0
        self.__quantity__ = 0
        self.__trade_margin__ = 0

    def get_available_margin(self):
        return self.__available_margin__
    
    def set_available_margin(self, available_margin):
        if available_margin == self.__available_margin__:
            return

        self.__available_margin__ = available_margin
        self.__on_changed__()

    def get_quantity(self):
        return self.__quantity__
    
    def set_quantity(self, quantity):
        if quantity == self.__quantity__:
            return

        self.__quantity__ = quantity
        self.__on_changed__()

    def get_trade_margin(self):
        return self.__trade_margin__
    
    def set_trade_margin(self, trade_margin):
        if trade_margin == self.__trade_margin__:
            return

        self.__trade_margin__ = trade_margin
        self.__on_changed__()

class button_styles():
    def create_button_style(self, color, hoverColor):
        style = Style(DefaultStyles.ButtonStyle)
        style.Set(ControlProperty.BackgroundColor, color, ControlState.DarkTheme)
        style.Set(ControlProperty.BackgroundColor, color, ControlState.LightTheme)
        style.Set(ControlProperty.BackgroundColor, hoverColor, ControlState.DarkTheme | ControlState.Hover)
        style.Set(ControlProperty.BackgroundColor, hoverColor, ControlState.LightTheme | ControlState.Hover)
        style.Set(ControlProperty.ForegroundColor, Color.FromHex("#FFFFFF"), ControlState.DarkTheme)
        style.Set(ControlProperty.ForegroundColor, Color.FromHex("#FFFFFF"), ControlState.LightTheme)
        style.Set(ControlProperty.Width, 100)
        style.Set(ControlProperty.Margin, Thickness(5, 0, 5, 0))
        return style

    def create_buy_button_style(self):
        return self.create_button_style(Color.FromHex("#009345"), Color.FromHex("#10A651"))

    def create_sell_button_style(self):
        return self.create_button_style(Color.FromHex("#F05824"), Color.FromHex("#FF6C36"))