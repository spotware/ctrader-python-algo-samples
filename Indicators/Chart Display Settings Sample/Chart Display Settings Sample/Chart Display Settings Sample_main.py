import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartDisplaySettingsSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.HorizontalAlignment = HorizontalAlignment.Left
        stackPanel.VerticalAlignment = VerticalAlignment.Bottom
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.7
        stackPanel.Margin = Thickness(5)
        stackPanel.Orientation = Orientation.Vertical

        askPriceLineCheckBox = CheckBox()
        askPriceLineCheckBox.Text = "Ask Price Line"
        askPriceLineCheckBox.Margin = Thickness(5)
        askPriceLineCheckBox.IsChecked = api.Chart.DisplaySettings.AskPriceLine
        askPriceLineCheckBox.Click += self.on_ask_price_line_check_box_click

        stackPanel.AddChild(askPriceLineCheckBox);

        bidPriceLineCheckBox = CheckBox()
        bidPriceLineCheckBox.Text = "Bid Price Line"
        bidPriceLineCheckBox.Margin = Thickness(5)
        bidPriceLineCheckBox.IsChecked = api.Chart.DisplaySettings.BidPriceLine
        bidPriceLineCheckBox.Click += self.on_bid_price_line_check_box_click

        stackPanel.AddChild(bidPriceLineCheckBox);

        chartScaleCheckBox = CheckBox()
        chartScaleCheckBox.Text = "Chart Scale"
        chartScaleCheckBox.Margin = Thickness(5)
        chartScaleCheckBox.IsChecked = api.Chart.DisplaySettings.ChartScale
        chartScaleCheckBox.Click += self.on_chart_scale_check_box_click

        stackPanel.AddChild(chartScaleCheckBox);

        dealMapCheckBox = CheckBox()
        dealMapCheckBox.Text = "Deal Map"
        dealMapCheckBox.Margin = Thickness(5)
        dealMapCheckBox.IsChecked = api.Chart.DisplaySettings.DealMap
        dealMapCheckBox.Click += self.on_deal_map_check_box_click

        stackPanel.AddChild(dealMapCheckBox);

        gridCheckBox = CheckBox()
        gridCheckBox.Text = "Grid"
        gridCheckBox.Margin = Thickness(5)
        gridCheckBox.IsChecked = api.Chart.DisplaySettings.Grid
        gridCheckBox.Click += self.on_grid_check_box_click

        stackPanel.AddChild(gridCheckBox)

        volumeCheckBox = CheckBox()
        volumeCheckBox.Text = "Volume"
        volumeCheckBox.Margin = Thickness(5)
        volumeCheckBox.IsChecked = api.Chart.DisplaySettings.TickVolume
        volumeCheckBox.Click += self.on_tick_volume_check_box_click

        stackPanel.AddChild(volumeCheckBox);

        api.Chart.AddControl(stackPanel);

    def on_ask_price_line_check_box_click(self, args):
        api.Chart.DisplaySettings.AskPriceLine = args.CheckBox.IsChecked

    def on_bid_price_line_check_box_click(self, args):
        api.Chart.DisplaySettings.BidPriceLine = args.CheckBox.IsChecked

    def on_chart_scale_check_box_click(self, args):
        api.Chart.DisplaySettings.ChartScale = args.CheckBox.IsChecked

    def on_deal_map_check_box_click(self, args):
        api.Chart.DisplaySettings.DealMap = args.CheckBox.IsChecked

    def on_grid_check_box_click(self, args):
        api.Chart.DisplaySettings.Grid = args.CheckBox.IsChecked

    def on_tick_volume_check_box_click(self, args):
        api.Chart.DisplaySettings.TickVolume = args.CheckBox.IsChecked