import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ServerSample():
    def initialize(self):
        grid = Grid(4, 2)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center

        self.style = Style()

        self.style.Set(ControlProperty.Padding, 5)
        self.style.Set(ControlProperty.Margin, 5)
        self.style.Set(ControlProperty.FontWeight, FontWeight.ExtraBold)
        self.style.Set(ControlProperty.BackgroundColor, Color.Black)

        titleTextBlock = self.get_text_block("Server Info")
        titleTextBlock.HorizontalAlignment = HorizontalAlignment.Center

        grid.AddChild(titleTextBlock, 0, 0, 1, 2)
        grid.AddChild(self.get_text_block("Time"), 1, 0)
        grid.AddChild(self.get_text_block(str(api.Server.Time)), 1, 1)
        grid.AddChild(self.get_text_block("Time (UTC)"), 2, 0)
        grid.AddChild(self.get_text_block(str(api.Server.TimeInUtc)), 2, 1)
        grid.AddChild(self.get_text_block("Is Connected"), 3, 0)

        self.isConnectedTextBlock = self.get_text_block("Yes" if api.Server.IsConnected else "No")

        api.Server.Connected += self.on_server_connected
        api.Server.Disconnected += self.on_server_disconnected

        grid.AddChild(self.isConnectedTextBlock, 3, 1)

        api.Chart.AddControl(grid)

    def on_server_connected(self):
        self.isConnectedTextBlock = "Yes"

    def on_server_disconnected(self):
        self.isConnectedTextBlock = "No"

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock