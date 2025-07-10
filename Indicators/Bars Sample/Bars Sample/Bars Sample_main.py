import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

def getTextBlock(text):
    textBlock = TextBlock()
    textBlock.Text = text
    textBlock.Margin = Thickness(5)
    return textBlock

class BarsSample():
    def initialize(self):
        api.Bars.BarOpened += self.barOpened
        api.Bars.Tick += self.barsTick
        api.Bars.HistoryLoaded += self.barsHistoryLoaded
        api.Bars.Reloaded += self.barsReloaded

        grid = Grid(2, 2)
        grid.BackgroundColor = Color.DarkGoldenrod
        grid.HorizontalAlignment = HorizontalAlignment.Right
        grid.VerticalAlignment = VerticalAlignment.Top
        grid.Opacity = 0.5

        grid.AddChild(getTextBlock("Bar Ticks #"), 0, 0)

        self.barTicksNumberTextBlock = getTextBlock("0")

        grid.AddChild(self.barTicksNumberTextBlock, 0, 1)
        grid.AddChild(getTextBlock("Bars State"), 1, 0)

        self.barsStateTextBlock = getTextBlock("")

        grid.AddChild(self.barsStateTextBlock, 1, 1)

        api.IndicatorArea.AddControl(grid)
        
    def calculate(self, index):
        api.Range[index] = api.Bars.HighPrices[index] - api.Bars.LowPrices[index]
        api.Body[index] = abs(api.Bars.ClosePrices[index] - api.Bars.OpenPrices[index])
    
    def barOpened(self, args):
        self.barsStateTextBlock.Text = "New Bar Opened"

    def barsTick(self, args):
        self.barTicksNumberTextBlock.Text = str(api.Bars.TickVolumes.LastValue)

    def barsHistoryLoaded(self, args):
        self.barsStateTextBlock.Text = "History Loaded"

    def barsReloaded(self, args):
        self.barsStateTextBlock.Text = "Reloaded"
