import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ActiveFrameChangedSample():
    def on_start(self):
        # Initialising the grid and the TextBlock displaying the percentage difference
        grid = Grid(1, 1)
        self.percentageTextBlock = TextBlock()
        self.percentageTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        self.percentageTextBlock.VerticalAlignment = VerticalAlignment.Center
        self.percentageTextBlock.Text = "Monthly change: "
            
        grid.AddChild(self.percentageTextBlock, 0, 0)
            
        # Initialising a new block inside the ASP and adding the grid as a child
        block = api.Asp.SymbolTab.AddBlock("Monthly Change Plugin")           
        block.Child = grid
            
        # Attaching an event handler to the ActiveFrameChanged event
        api.ChartManager.ActiveFrameChanged += self.on_chart_manager_active_frame_changed
        
    def on_chart_manager_active_frame_changed(self, args):
        if args.NewFrame is None or isinstance(args.NewFrame.__implementation__, ChartFrame) == False:
            return
            
        newChartFrame = ChartFrame(args.NewFrame)
                
        # Attaining market data for the symbol for which the currently active ChartFrame is opened
        dailySeries = api.MarketData.GetBars(TimeFrame.Daily, newChartFrame.Symbol.Name)
                
        # Calculating the monthly change and displaying it inside the TextBlock
        monthlyChange = (newChartFrame.Symbol.Bid - dailySeries.ClosePrices[dailySeries.ClosePrices.Count - 30]) / 100
        self.percentageTextBlock.Text = f"Monthly change: {monthlyChange}"
