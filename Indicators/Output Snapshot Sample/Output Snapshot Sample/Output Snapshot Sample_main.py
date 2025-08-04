import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from math import nan

class OutputSnapshotSample():
    def initialize(self):
        self.toleranceInPips = api.ToleranceInPips * api.Symbol.PipSize
        self.ma = api.Indicators.MovingAverage(api.Bars.ClosePrices, 9, MovingAverageType.Exponential)
        
        self.marketSnapshotControl = MarketSnapshotControl()
        self.marketSnapshotControl.content.BackgroundColor = Color.Gold
        self.marketSnapshotControl.content.BorderColor = Color.Gray
        self.marketSnapshotControl.content.VerticalAlignment = VerticalAlignment.Top
        self.marketSnapshotControl.content.HorizontalAlignment = HorizontalAlignment.Left
        self.marketSnapshotControl.content.Opacity = 0.6
        self.marketSnapshotControl.content.Margin = Thickness(2)
        self.marketSnapshotControl.content.IsVisible = False
        self.marketSnapshotControl.content.Width = 220
        self.marketSnapshotControl.content.Height = 50

        api.IndicatorArea.AddControl(self.marketSnapshotControl.content)

        api.IndicatorArea.MouseMove += self.on_indicator_area_mouse_move
        api.IndicatorArea.MouseLeave += self.on_indicator_area_mouse_leave

    def calculate(self, index):
        api.Main[index] = self.ma.Result[index]

    def on_indicator_area_mouse_move(self, args):
        index = int(args.BarIndex)
        yValue = round(args.YValue, api.Symbol.Digits)
        mainValue = round(api.Main[index], api.Symbol.Digits)

        if mainValue == nan or abs(mainValue - yValue) > self.toleranceInPips:
            self.marketSnapshotControl.content.IsVisible = False
            return

        extraDelta = 10
        width = self.marketSnapshotControl.content.Width
        height = self.marketSnapshotControl.content.Height
        left = args.MouseX + extraDelta if api.Chart.Width - args.MouseX > width + extraDelta else args.MouseX - width - extraDelta
        right = args.MouseY + extraDelta if api.Chart.Height - args.MouseY > height + extraDelta else args.MouseY - height - extraDelta

        self.marketSnapshotControl.content.Margin = Thickness(left, right, 0, 0)

        self.marketSnapshotControl.set_time(api.Bars.OpenTimes[index].ToString("g"))
        self.marketSnapshotControl.set_value(str(api.Main[index]))
        self.marketSnapshotControl.content.IsVisible = True

    def on_indicator_area_mouse_leave(self, args):
        self.marketSnapshotControl.content.IsVisible = False

class MarketSnapshotControl():
    def __init__(self):
        self.content = Border()
        self.content.BackgroundColor = Color.FromHex("#3F3F3F")
        self.content.BorderColor = Color.FromHex("#969696")
        self.content.BorderThickness = Thickness(1)
        self.content.CornerRadius = CornerRadius(5)

        style = Style()

        style.Set(ControlProperty.Margin, Thickness(3, 3, 0, 0))
        style.Set(ControlProperty.FontWeight, FontWeight.Bold)
        style.Set(ControlProperty.ForegroundColor, Color.Black)
        style.Set(ControlProperty.HorizontalContentAlignment, HorizontalAlignment.Left)
        style.Set(ControlProperty.VerticalContentAlignment, VerticalAlignment.Center)

        self.valueTextBlock = TextBlock()
        self.valueTextBlock.Style = style

        self.timeTextBlock = TextBlock()
        self.timeTextBlock.Style = style

        grid = Grid(2, 2)
        grid.ShowGridLines = True

        grid.AddChild(self.get_text_block("Value", style), 0, 0)
        grid.AddChild(self.get_text_block("Time", style), 1, 0)

        grid.AddChild(self.valueTextBlock, 0, 1);
        grid.AddChild(self.timeTextBlock, 1, 1);

        self.content.Child = grid;

    def get_text_block(self, text, style):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.style = style
        return textBlock

    def set_value(self, value):
        self.valueTextBlock.Text = value

    def set_time(self, value):
        self.timeTextBlock.Text = value