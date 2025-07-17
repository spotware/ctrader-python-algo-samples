import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CoordinatesConversionSample():
    def on_start(self):
        self.is_mouse_hover = False
        # Initialising the TextBlock and setting its parameters
        self.priceInfoTextBlock = TextBlock()
        self.priceInfoTextBlock.TextAlignment = TextAlignment.Center
        self.priceInfoTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        self.priceInfoTextBlock.VerticalAlignment = VerticalAlignment.Center
        self.priceInfoTextBlock.Text = "Initialising..."
        self.priceInfoTextBlock.FontSize = 26
        self.priceInfoTextBlock.FontWeight = FontWeight.Bold

        # Adding a new tab into TradeWatch and setting the TextBlock as its child
        tradeWatchTab = api.TradeWatch.AddTab("EURUSD Hover Price")
        tradeWatchTab.Child = self.priceInfoTextBlock
            
        # Opening a new ChartFrame and storing its Chart
        eurusdChartFrame = api.ChartManager.AddChartFrame("EURUSD", TimeFrame.Hour)
        eurusdChart = eurusdChartFrame.Chart
            
        eurusdChart.MouseEnter += self.on_chart_mouse_enter
        eurusdChart.MouseLeave += self.on_chart_mouse_leave
        eurusdChart.MouseMove += self.on_chart_mouse_move

    def on_chart_mouse_enter(self, args):
        self.is_mouse_hover = True
        self.show_mouse_position_info(args)

    def on_chart_mouse_leave(self, args):
        self.is_mouse_hover = False
        self.show_unavailable(args.Chart.SymbolName)

    def on_chart_mouse_move(self, args):
        if self.is_mouse_hover == False:
            return
        self.show_mouse_position_info(args)
    
    def show_unavailable(self, symbolName):
        # Displaying special text when the mouse cursor leaves the chart or index is out of bars range
        self.priceInfoTextBlock.Text = f"{symbolName} Price: Unavavailable"

    def show_mouse_position_info(self, args):
        # Attaining the Bars for EURUSD and determining the bar index over which the mouse cursor is hovering
        bars = args.Chart.Bars
        hoverIndex = int(args.Chart.XToBarIndex(args.MouseX))

        if hoverIndex >= bars.Count:
            self.show_unavailable(args.Chart.SymbolName)
            return
        # Updating the text inside the TextBlock
        self.priceInfoTextBlock.Text = f"""{args.Chart.SymbolName} Price at {hoverIndex}:
         {bars[hoverIndex].OpenTime}
         {bars[hoverIndex].Open}
         {bars[hoverIndex].Close}
         {bars[hoverIndex].High}
         {bars[hoverIndex].Low}"""
