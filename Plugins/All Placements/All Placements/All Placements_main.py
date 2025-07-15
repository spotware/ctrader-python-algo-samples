import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

from System import Func, Action

class AllPlacements():
    def on_start(self):
        api.Commands.Add(CommandType.ChartContainerToolbar, Func[CommandArgs, CommandResult](self.command_handler), COMMANDSVGICON);

    def command_handler(self, args):
        buttonStyle = Style()
        buttonStyle.Set(ControlProperty.Margin, Thickness(0, 5, 0, 0))
        buttonStyle.Set(ControlProperty.Width, 150)

        stackPanel = StackPanel()

        showMessageBoxButton = Button()
        showMessageBoxButton.Text = "show MessageBox"
        showMessageBoxButton.Style = buttonStyle
        showMessageBoxButton.Click += lambda _ : MessageBox.Show("Some message", "Caption", MessageBoxButton.YesNo)

        stackPanel.AddChild(showMessageBoxButton)

        showCustomWindowButton = Button()
        showCustomWindowButton.Text = "show Custom Window"
        showCustomWindowButton.Style = buttonStyle
        showCustomWindowButton.Click += self.on_show_window_button_clicked

        stackPanel.AddChild(showCustomWindowButton)

        self.blockCounter = 1

        addAspBlockButton = Button()
        addAspBlockButton.Text = "add ASP Block"
        addAspBlockButton.Style = buttonStyle
        addAspBlockButton.Click += self.on_add_asp_block_button_clicked

        stackPanel.AddChild(addAspBlockButton)

        self.aspTabCounter = 1
        
        addAspTabButton = Button()
        addAspTabButton.Text = "add ASP Tab"
        addAspTabButton.Style = buttonStyle
        addAspTabButton.Click += self.on_add_asp_tab_button_clicked
        
        stackPanel.AddChild(addAspTabButton)

        self.tradewatchTabCounter = 1

        addTradeWatchTabButton = Button()
        addTradeWatchTabButton.Text = "add TradeWatch Tab"
        addTradeWatchTabButton.Style = buttonStyle
        addTradeWatchTabButton.Click += self.on_add_trade_watch_tab_button
        
        stackPanel.AddChild(addTradeWatchTabButton)

        self.customFrameCounter = 1;

        addCustomFrameButton = Button()
        addCustomFrameButton.Text = "add Custom Frame"
        addCustomFrameButton.Style = buttonStyle
        addCustomFrameButton.Click += self.on_add_custom_frame_button_clicked
        
        stackPanel.AddChild(addCustomFrameButton);

        self.mainMenuItemCounter = 1;

        addMainMenuItemButton = Button()
        addMainMenuItemButton.Text = "add Main Menu Item"
        addMainMenuItemButton.Style = buttonStyle
        addMainMenuItemButton.Click += self.on_add_main_menu_item_button_clicked
        
        stackPanel.AddChild(addMainMenuItemButton);

        self.mainMenuBottomItemCounter = 1;

        addMainMenuBottomItemButton = Button()
        addMainMenuBottomItemButton.Text = "add Main Menu Bottom Item"
        addMainMenuBottomItemButton.Style = buttonStyle
        addMainMenuBottomItemButton.Click += self.on_add_main_menu_bottom_item_button_clicked
        
        stackPanel.AddChild(addMainMenuBottomItemButton);

        customizeActiveChartButton = Button()
        customizeActiveChartButton.Text = "customize Active Chart"
        customizeActiveChartButton.Style = buttonStyle
        customizeActiveChartButton.Click += self.on_customize_active_chart_button_clicked
        
        stackPanel.AddChild(customizeActiveChartButton);

        border = Border()
        border.Padding = Thickness(5)
        border.BackgroundColor = Color.FromHex("#1A1A1A")
        border.CornerRadius = CornerRadius(3)
        border.BorderThickness = Thickness(1)
        border.BorderColor = Color.FromHex("#525252")
        border.Child = stackPanel
        border.Width = 170
        border.Height = 250
        
        return CommandResult(border);

    def on_show_window_button_clicked(self, args):
        window = Window()
        webView = WebView()
        window.Child = webView

        window.Show()
        webView.NavigateAsync(WEBVIEWURL)

    def on_add_asp_block_button_clicked(self, args):
        newBlock = api.Asp.SymbolTab.AddBlock(f"One more block {self.blockCounter}")
        newBlock.IsExpanded = True
        newBlock.Height = 600
        self.blockCounter += 1
        webView = WebView()
        newBlock.Child = webView
        webView.NavigateAsync(WEBVIEWURL)

    def on_add_asp_tab_button_clicked(self, args):
        tab = api.Asp.AddTab(f"ASP tab {self.aspTabCounter}")
        tab.Index = self.aspTabCounter
        self.aspTabCounter += 1
        webView = WebView()
        tab.Child = webView
        webView.NavigateAsync(WEBVIEWURL)

    def on_add_trade_watch_tab_button(self, args):
        tab = api.TradeWatch.AddTab(f"Tab {self.tradewatchTabCounter}")
        tab.Index = self.tradewatchTabCounter
        self.tradewatchTabCounter += 1
        tab.IsSelected = True
        webView = WebView()
        tab.Child = webView
        webView.NavigateAsync(WEBVIEWURL)

    def on_add_custom_frame_button_clicked(self, args):
        frame = api.ChartManager.AddCustomFrame(f"Custom Frame {self.customFrameCounter}")
        self.customFrameCounter += 1
        webView = WebView()
        frame.Child = webView
        webView.NavigateAsync(WEBVIEWURL)

    def on_customize_active_chart_button_clicked(self, args):
        activeFrame = api.ChartManager.ActiveFrame

        if activeFrame is None or isinstance(activeFrame.__implementation__, ChartFrame) == False:
            return
            
        chartFrame = ChartFrame(activeFrame)
        chart = chartFrame.Chart
        chart.ColorSettings.BackgroundColor = Color.DarkBlue
        chart.DisplaySettings.TickVolume = False
        chart.ZoomLevel = 10

    def on_add_main_menu_item_button_clicked(self, args):
        item = api.MainMenu.AddItem(f"Item {self.mainMenuItemCounter}", MAINMENUITEMSVGICON)
        self.mainMenuItemCounter += 1
        webView = WebView()
        webView.Loaded += lambda _ : webView.NavigateAsync("https://help.ctrader.com/")
        item.Child = webView

    def main_menu_bottom_item_handler(self):
        api.Print("Main menu bottom item triggered!")

    def on_add_main_menu_bottom_item_button_clicked(self, args):
        item = api.MainMenu.AddBottomItem(f"Item {self.mainMenuBottomItemCounter}", MAINMENUBOTTOMITEMSVGICON)
        self.mainMenuBottomItemCounter += 1
        item.Handler = Action(self.main_menu_bottom_item_handler)

    

WEBVIEWURL = "https://ctrader.com";

COMMANDSVGICON = SvgIcon("<svg class='w-6 h-6 text-gray-800 dark:text-white' aria-hidden='true' xmlns='http://www.w3.org/2000/svg' width='15' height='15' fill='none' viewBox='0 0 24 24'><path stroke='#BFBFBF' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M11 6.5h2M11 18h2m-7-5v-2m12 2v-2M5 8h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm0 12h2a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm12 0h2a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm0-12h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Z'/></svg>")
MAINMENUITEMSVGICON = SvgIcon("<svg width=\"800px\" height=\"800px\" viewBox=\"0 0 1024 1024\" class=\"icon\"  version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M819.9 747.6H204.1c-21.8 0-39.5-17.7-39.5-39.5V278.4c0-21.8 17.7-39.5 39.5-39.5h615.7c21.8 0 39.5 17.7 39.5 39.5v429.7c0.1 21.9-17.6 39.5-39.4 39.5z\" fill=\"#FFD632\" /><path d=\"M819.9 753.1H204.1c-24.8 0-45-20.2-45-45V278.4c0-24.8 20.2-45 45-45h615.7c24.8 0 45 20.2 45 45v429.7c0.1 24.9-20.1 45-44.9 45zM204.1 244.4c-18.7 0-34 15.3-34 34v429.7c0 18.7 15.3 34 34 34h615.7c18.7 0 34-15.3 34-34V278.4c0-18.7-15.3-34-34-34H204.1z\" fill=\"#333336\" /><path d=\"M296.5 766.6h58.3v39.9c0 10.1-8.2 18.4-18.4 18.4h-21.6c-10.1 0-18.4-8.2-18.4-18.4v-39.9z\" fill=\"#FFC86B\" /><path d=\"M336.4 830.4h-21.6c-13.2 0-23.9-10.7-23.9-23.9v-45.4h69.3v45.4c0.1 13.2-10.6 23.9-23.8 23.9zM302 772.1v34.4c0 7.1 5.8 12.9 12.9 12.9h21.6c7.1 0 12.9-5.8 12.9-12.9v-34.4H302z\" fill=\"#333336\" /><path d=\"M441 315.3v-62.1c0-29.4-23.9-53.3-53.3-53.3H263.6c-29.4 0-53.3 23.9-53.3 53.3v62.1c0 24.7 7.8 47.6 21 66.4 6.5 9.2 9.9 20.3 9.9 31.5v160.2c0 11.3-3.4 22.3-9.9 31.5-13.2 18.8-21 41.7-21 66.4v63.1c0 28.9 23.4 52.3 52.3 52.3h126.2c28.9 0 52.3-23.4 52.3-52.3v-63.1c0-24.7-7.7-47.5-20.9-66.2-6.5-9.3-10-20.4-10-31.8v-160c0-11.4 3.4-22.5 10-31.8 13-18.8 20.8-41.6 20.8-66.2z\" fill=\"#68A240\" /><path d=\"M388.7 792.1H262.6c-31.8 0-57.8-25.9-57.8-57.8v-63.1c0-25.1 7.6-49.1 22-69.5 5.8-8.2 8.9-18 8.9-28.4V413.2c0-10.3-3.1-20.1-8.9-28.4-14.4-20.4-22-44.5-22-69.5v-62.1c0-32.4 26.4-58.8 58.8-58.8h124.1c32.4 0 58.8 26.4 58.8 58.8v62.1c0 25-7.6 49-21.9 69.4-5.9 8.3-9 18.2-9 28.7v159.9c0 10.4 3.1 20.3 9 28.7 14.3 20.4 21.9 44.4 21.9 69.4v63.1c0 31.7-25.9 57.6-57.8 57.6zM263.6 205.4c-26.3 0-47.8 21.4-47.8 47.8v62.1c0 22.8 6.9 44.6 20 63.2 7.1 10.1 10.9 22.1 10.9 34.7v160.2c0 12.6-3.8 24.6-10.9 34.7-13.1 18.6-20 40.4-20 63.2v63.1c0 25.8 21 46.8 46.8 46.8h126.2c25.8 0 46.8-21 46.8-46.8v-63.1c0-22.7-6.9-44.5-19.9-63.1-7.2-10.2-11-22.3-11-35V413.3c0-12.7 3.8-24.8 11-35 13-18.5 19.9-40.3 19.9-63.1v-62.1c0-26.3-21.4-47.8-47.8-47.8H263.6z\" fill=\"#333336\" /><path d=\"M780.6 437.5H495.4c-8 0-14.5-6.5-14.5-14.5V317.6c0-8 6.5-14.5 14.5-14.5h285.2c8 0 14.5 6.5 14.5 14.5V423c0 8-6.5 14.5-14.5 14.5z\" fill=\"#D8A128\" /><path d=\"M780.6 443H495.4c-11 0-20-9-20-20V317.6c0-11 9-20 20-20h285.2c11 0 20 9 20 20V423c0 11-8.9 20-20 20zM495.4 308.6c-5 0-9 4-9 9V423c0 5 4 9 9 9h285.2c5 0 9-4 9-9V317.6c0-5-4-9-9-9H495.4zM476.9 889.6c-2.1 0-4-1.2-5-3.2-0.8-1.6-19.7-39-79-19.6-23.1 7.5-41.3 6.6-54.3-2.8-18.3-13.2-18.5-38-18.5-39.1 0-3 2.5-5.5 5.5-5.5s5.5 2.5 5.5 5.5c0 0.3 0.3 20.4 14 30.2 10 7.2 24.9 7.6 44.4 1.2 19.6-6.4 48.1-11 71.8 3.8 14.5 9 20.3 21 20.5 21.5 1.3 2.7 0.1 6-2.6 7.3-0.8 0.5-1.6 0.7-2.3 0.7z m-145.7-64.7z\" fill=\"#333336\" /><path d=\"M550 570.9h-57.3c-4.7 0-8.6-3.8-8.6-8.6V505c0-4.7 3.8-8.6 8.6-8.6H550c4.7 0 8.6 3.8 8.6 8.6v57.3c-0.1 4.7-3.9 8.6-8.6 8.6z\" fill=\"#D5D9CF\" /><path d=\"M550 576.4h-57.3c-7.8 0-14.1-6.3-14.1-14.1V505c0-7.8 6.3-14.1 14.1-14.1H550c7.8 0 14.1 6.3 14.1 14.1v57.3c-0.1 7.8-6.4 14.1-14.1 14.1z m-57.3-74.5c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1H550c1.7 0 3.1-1.4 3.1-3.1V505c0-1.7-1.4-3.1-3.1-3.1h-57.3z\" fill=\"#333336\" /><path d=\"M667.3 570.9H610c-4.7 0-8.6-3.8-8.6-8.6V505c0-4.7 3.8-8.6 8.6-8.6h57.3c4.7 0 8.6 3.8 8.6 8.6v57.3c0 4.7-3.8 8.6-8.6 8.6z\" fill=\"#D5D9CF\" /><path d=\"M667.3 576.4H610c-7.8 0-14.1-6.3-14.1-14.1V505c0-7.8 6.3-14.1 14.1-14.1h57.3c7.8 0 14.1 6.3 14.1 14.1v57.3c0 7.8-6.3 14.1-14.1 14.1zM610 501.9c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1h57.3c1.7 0 3.1-1.4 3.1-3.1V505c0-1.7-1.4-3.1-3.1-3.1H610z\" fill=\"#333336\" /><path d=\"M784.7 570.9h-57.3c-4.7 0-8.6-3.8-8.6-8.6V505c0-4.7 3.8-8.6 8.6-8.6h57.3c4.7 0 8.6 3.8 8.6 8.6v57.3c0 4.7-3.9 8.6-8.6 8.6z\" fill=\"#D5D9CF\" /><path d=\"M784.7 576.4h-57.3c-7.8 0-14.1-6.3-14.1-14.1V505c0-7.8 6.3-14.1 14.1-14.1h57.3c7.8 0 14.1 6.3 14.1 14.1v57.3c0 7.8-6.3 14.1-14.1 14.1z m-57.3-74.5c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1h57.3c1.7 0 3.1-1.4 3.1-3.1V505c0-1.7-1.4-3.1-3.1-3.1h-57.3z\" fill=\"#333336\" /><path d=\"M550 691.6h-57.3c-4.7 0-8.6-3.8-8.6-8.6v-57.3c0-4.7 3.8-8.6 8.6-8.6H550c4.7 0 8.6 3.8 8.6 8.6V683c-0.1 4.8-3.9 8.6-8.6 8.6z\" fill=\"#D5D9CF\" /><path d=\"M550 697.1h-57.3c-7.8 0-14.1-6.3-14.1-14.1v-57.3c0-7.8 6.3-14.1 14.1-14.1H550c7.8 0 14.1 6.3 14.1 14.1V683c-0.1 7.8-6.4 14.1-14.1 14.1z m-57.3-74.4c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1H550c1.7 0 3.1-1.4 3.1-3.1v-57.3c0-1.7-1.4-3.1-3.1-3.1h-57.3z\" fill=\"#333336\" /><path d=\"M667.3 691.6H610c-4.7 0-8.6-3.8-8.6-8.6v-57.3c0-4.7 3.8-8.6 8.6-8.6h57.3c4.7 0 8.6 3.8 8.6 8.6V683c0 4.8-3.8 8.6-8.6 8.6z\" fill=\"#D5D9CF\" /><path d=\"M667.3 697.1H610c-7.8 0-14.1-6.3-14.1-14.1v-57.3c0-7.8 6.3-14.1 14.1-14.1h57.3c7.8 0 14.1 6.3 14.1 14.1V683c0 7.8-6.3 14.1-14.1 14.1zM610 622.7c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1h57.3c1.7 0 3.1-1.4 3.1-3.1v-57.3c0-1.7-1.4-3.1-3.1-3.1H610z\" fill=\"#333336\" /><path d=\"M784.7 691.6h-57.3c-4.7 0-8.6-3.8-8.6-8.6v-57.3c0-4.7 3.8-8.6 8.6-8.6h57.3c4.7 0 8.6 3.8 8.6 8.6V683c0 4.8-3.9 8.6-8.6 8.6z\" fill=\"#68A240\" /><path d=\"M784.7 697.1h-57.3c-7.8 0-14.1-6.3-14.1-14.1v-57.3c0-7.8 6.3-14.1 14.1-14.1h57.3c7.8 0 14.1 6.3 14.1 14.1V683c0 7.8-6.3 14.1-14.1 14.1z m-57.3-74.4c-1.7 0-3.1 1.4-3.1 3.1v57.3c0 1.7 1.4 3.1 3.1 3.1h57.3c1.7 0 3.1-1.4 3.1-3.1v-57.3c0-1.7-1.4-3.1-3.1-3.1h-57.3z\" fill=\"#333336\" /></svg>")
MAINMENUBOTTOMITEMSVGICON = SvgIcon("<svg width=\"800px\" height=\"800px\" viewBox=\"0 0 1024 1024\" class=\"icon\"  version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M819 234l-48-13 48-13 13-48 13 48 48 13-48 13-13 48-13-48zM867 287l-19-5 19-4 4-19 4 19 19 4-19 5-4 19-4-19z\" fill=\"#FDCD60\" /><path d=\"M130 472l-21-5 21-5 5-21 5 21 21 5-21 5-5 20-5-20z\" fill=\"#FDCD60\" /><path d=\"M208 246m-9 0a9 9 0 1 0 18 0 9 9 0 1 0-18 0Z\" fill=\"#5546CB\" /><path d=\"M824 804a25 25 0 1 1 25-25 25 25 0 0 1-25 25z m0-36a10 10 0 1 0 10 10 10 10 0 0 0-10-9z\" fill=\"#5546CB\" /><path d=\"M166 728h78v77.34h-78z\" fill=\"#FDCD60\" /><path d=\"M452 509v43h128v-43a19 19 0 0 1 14-18H438a19 19 0 0 1 14 18z\" fill=\"#F97744\" /><path d=\"M661 489h1a19 19 0 0 1 19 19v43h32v114a74 74 0 0 1-74 74H387a73 73 0 0 1-73-73V552h38v-43a19 19 0 0 1 19-19h1a116 116 0 0 1-83-50v337a31 31 0 0 0 31 31h386a31 31 0 0 0 31-31V440a116 116 0 0 1-76 49z\" fill=\"#F97744\" /><path d=\"M334 666a53 53 0 0 0 53 53h251a54 54 0 0 0 54-54v-93h-32a30 30 0 0 1-30 25 30 30 0 0 1-30-25H432a30 30 0 0 1-30 25 30 30 0 0 1-30-25h-38z\" fill=\"#FFFFFF\" /><path d=\"M580 553H452a19 19 0 0 1-19 19h166a19 19 0 0 1-19-19z\" fill=\"#5546CB\" /><path d=\"M662 572h30v93a54 54 0 0 1-54 54H387a53 53 0 0 1-53-53v-94h37a19 19 0 0 1-19-19h-38v113a73 73 0 0 0 73 73h251a74 74 0 0 0 74-74V552h-32a19 19 0 0 1-18 20z\" fill=\"#5546CB\" /><path d=\"M289 375a96 96 0 0 0 83 95v-70a30 30 0 0 1 30-30 30 30 0 0 1 30 30v71h168v-71a30 30 0 0 1 30-30 30 30 0 0 1 30 30v69a96 96 0 0 0 76-94V266a31 31 0 0 0-31-31H320a31 31 0 0 0-31 31v109z\" fill=\"#FDCD60\" /><path d=\"M402 597a30 30 0 0 0 30-25h-59a30 30 0 0 0 29 25zM372 510h60v41.48h-60zM630 597a30 30 0 0 0 30-25h-59a30 30 0 0 0 29 25zM600 510h60v41.48h-60z\" fill=\"#5546CB\" /><path d=\"M438 491h-67a19 19 0 0 0-19 19v43a19 19 0 0 0 19 19h63a19 19 0 0 0 19-19v-44a19 19 0 0 0-15-18z m-6 61h-60v-42h60zM662 490h-67a19 19 0 0 0-14 18v43a19 19 0 0 0 19 19h63a19 19 0 0 0 19-19v-42a19 19 0 0 0-20-19z m-1 61h-61v-41h60z\" fill=\"#FDCD60\" /><path d=\"M786 524h-29v148h29a24 24 0 0 0 24-24V548a24 24 0 0 0-24-24z\" fill=\"#AFBCF3\" /><path d=\"M786 504h-29V266a51 51 0 0 0-51-51h-78a116 116 0 0 0-230 0h-78a51 51 0 0 0-51 51v240l-8-2h-30a44 44 0 0 0-44 44v100a44 44 0 0 0 44 44h30l8-2v87a51 51 0 0 0 51 51h386a51 51 0 0 0 51-51v-85h29a44 44 0 0 0 44-44V548a44 44 0 0 0-44-44zM260 672h-29a24 24 0 0 1-24-24V548a24 24 0 0 1 24-24h29z m253-536a96 96 0 0 1 95 79H418a96 96 0 0 1 95-79zM289 266a31 31 0 0 1 31-31h386a31 31 0 0 1 31 31v109a96 96 0 0 1-76 94v-69a30 30 0 0 0-30-30 30 30 0 0 0-30 30v71H432v-71a30 30 0 0 0-30-30 30 30 0 0 0-30 30v70a96 96 0 0 1-83-95V266z m417 542H320a31 31 0 0 1-31-31V440a116 116 0 0 0 83 50h289a116 116 0 0 0 76-49v336a31 31 0 0 1-31 31z m104-160a24 24 0 0 1-24 24h-29V524h29a24 24 0 0 1 24 24z\" fill=\"#5546CB\" /><path d=\"M208 548v100a24 24 0 0 0 24 24h29V524h-30a24 24 0 0 0-23 24z\" fill=\"#AFBCF3\" /></svg>")