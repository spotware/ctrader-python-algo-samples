import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MarketSnapshotSample():
    def initialize(self):
        self.marketSnapshotControl = MarketSnapshotControl()
        self.marketSnapshotControl.content.BackgroundColor = Color.Gold
        self.marketSnapshotControl.content.BorderColor = Color.Gray
        self.marketSnapshotControl.content.VerticalAlignment = VerticalAlignment.Top
        self.marketSnapshotControl.content.HorizontalAlignment = HorizontalAlignment.Left
        self.marketSnapshotControl.content.Opacity = 0.6
        self.marketSnapshotControl.content.Margin = Thickness(2)
        self.marketSnapshotControl.content.IsVisible = False
        self.marketSnapshotControl.content.Width = 220
        self.marketSnapshotControl.content.Height = 200

        api.Chart.AddControl(self.marketSnapshotControl.content)

        api.Chart.MouseDown += self.on_chart_mouse_down
        api.Chart.MouseUp += self.on_chart_mouse_up

    def on_chart_mouse_down(self, args):
        extraDelta = 10
        width = self.marketSnapshotControl.content.Width
        height = self.marketSnapshotControl.content.Height
        left = args.MouseX + extraDelta if api.Chart.Width - args.MouseX > width + extraDelta else args.MouseX - width - extraDelta
        right = args.MouseY + extraDelta if api.Chart.Height - args.MouseY > height + extraDelta else args.MouseY - height - extraDelta

        self.marketSnapshotControl.content.Margin = Thickness(left, right, 0, 0)

        index = int(args.BarIndex)

        self.marketSnapshotControl.set_open(str(api.Bars.OpenPrices[index]))
        self.marketSnapshotControl.set_high(str(api.Bars.HighPrices[index]))
        self.marketSnapshotControl.set_low(str(api.Bars.LowPrices[index]))
        self.marketSnapshotControl.set_close(str(api.Bars.ClosePrices[index]))
        self.marketSnapshotControl.set_time(api.Bars.OpenTimes[index].ToString("g"))
        self.marketSnapshotControl.set_volume(str(api.Bars.TickVolumes[index]))
        self.marketSnapshotControl.content.IsVisible = True

    def on_chart_mouse_up(self, args):
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

        self.openTextBlock = TextBlock()
        self.openTextBlock.Style = style

        self.highTextBlock = TextBlock()
        self.highTextBlock.Style = style

        self.lowTextBlock = TextBlock()
        self.lowTextBlock.Style = style

        self.closeTextBlock = TextBlock()
        self.closeTextBlock.Style = style

        self.volumeTextBlock = TextBlock()
        self.volumeTextBlock.Style = style

        self.timeTextBlock = TextBlock()
        self.timeTextBlock.Style = style

        grid = Grid(6, 2)
        grid.ShowGridLines = True

        grid.AddChild(self.get_text_block("Open", style), 0, 0)
        grid.AddChild(self.get_text_block("High", style), 1, 0)
        grid.AddChild(self.get_text_block("Low", style), 2, 0)
        grid.AddChild(self.get_text_block("Close", style), 3, 0)
        grid.AddChild(self.get_text_block("Volume", style), 4, 0)
        grid.AddChild(self.get_text_block("Time", style), 5, 0)

        grid.AddChild(self.openTextBlock, 0, 1);
        grid.AddChild(self.highTextBlock, 1, 1);
        grid.AddChild(self.lowTextBlock, 2, 1);
        grid.AddChild(self.closeTextBlock, 3, 1);
        grid.AddChild(self.volumeTextBlock, 4, 1);
        grid.AddChild(self.timeTextBlock, 5, 1);

        self.content.Child = grid;

    def get_text_block(self, text, style):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.style = style
        return textBlock

    def set_open(self, value):
        self.openTextBlock.Text = value

    def set_high(self, value):
        self.highTextBlock.Text = value

    def set_low(self, value):
        self.lowTextBlock.Text = value

    def set_close(self, value):
        self.closeTextBlock.Text = value

    def set_volume(self, value):
        self.volumeTextBlock.Text = value

    def set_time(self, value):
        self.timeTextBlock.Text = value