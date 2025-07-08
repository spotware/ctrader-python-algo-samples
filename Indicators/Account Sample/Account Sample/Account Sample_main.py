import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AccountSample():
    def initialize(self):
        grid = Grid(16, 2)
        grid.BackgroundColor = Color.Gold
        grid.Opacity = 0.6
        grid.HorizontalAlignment = HorizontalAlignment.Center
        grid.VerticalAlignment = VerticalAlignment.Center
        
        self.style = Style()

        self.style.Set(ControlProperty.Padding, 5)
        self.style.Set(ControlProperty.Margin, 5)
        self.style.Set(ControlProperty.FontWeight, FontWeight.ExtraBold)
        self.style.Set(ControlProperty.BackgroundColor, Color.Black)

        headerTextBox = self.getTextBlock("Account Info")
        headerTextBox.HorizontalAlignment = HorizontalAlignment.Center

        grid.AddChild(headerTextBox, 0, 0, 1, 2)
        grid.AddChild(self.getTextBlock("Type"), 1, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.AccountType)), 1, 1)
        grid.AddChild(self.getTextBlock("Is Live"), 2, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.IsLive)), 2, 1)
        grid.AddChild(self.getTextBlock("Balance"), 3, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.Balance)), 3, 1)
        grid.AddChild(self.getTextBlock("Broker Name"), 4, 0)
        grid.AddChild(self.getTextBlock(api.Account.BrokerName), 4, 1)
        grid.AddChild(self.getTextBlock("Currency"), 5, 0)
        grid.AddChild(self.getTextBlock(api.Account.Asset.Name), 5, 1)
        grid.AddChild(self.getTextBlock("Number"), 6, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.Number)), 6, 1)
        grid.AddChild(self.getTextBlock("Equity"), 7, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.Equity)), 7, 1)
        grid.AddChild(self.getTextBlock("Free Margin"), 8, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.FreeMargin)), 8, 1)
        grid.AddChild(self.getTextBlock("Margin"), 9, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.Margin)), 9, 1)
        grid.AddChild(self.getTextBlock("Margin Level"), 10, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.MarginLevel)), 10, 1)
        grid.AddChild(self.getTextBlock("Precise Leverage"), 11, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.PreciseLeverage)), 11, 1)
        grid.AddChild(self.getTextBlock("Stop Out Level"), 12, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.StopOutLevel)), 12, 1)
        grid.AddChild(self.getTextBlock("Unrealized Gross Profit"), 13, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.UnrealizedGrossProfit)), 13, 1)
        grid.AddChild(self.getTextBlock("Unrealized Net Profit"), 14, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.UnrealizedNetProfit)), 14, 1)
        grid.AddChild(self.getTextBlock("User Id"), 15, 0)
        grid.AddChild(self.getTextBlock(str(api.Account.UserId)), 15, 1)

        api.Chart.AddControl(grid)
        
    def calculate(self, index):
        pass

    def getTextBlock(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock