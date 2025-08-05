import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SmoothMouseMoveSample():
    def initialize(self):
        # Initialising the Border and setting  its parameters
        self.gridStatusBorder = Border()
        self.gridStatusBorder.IsHitTestVisible = False
        self.gridStatusBorder.CornerRadius = CornerRadius(3)
        self.gridStatusBorder.BorderThickness = Thickness(1)
        self.gridStatusBorder.Padding = Thickness(5)
        self.gridStatusBorder.Margin = Thickness(5, 5, 0, 0)
        self.gridStatusBorder.BackgroundColor = api.Chart.ColorSettings.BackgroundColor
        self.gridStatusBorder.BorderColor = api.Chart.ColorSettings.ForegroundColor
        self.gridStatusBorder.IsVisible = False

        # Configuring the Grid for placing the text blocks
        grid = Grid()
        grid.ShowGridLines = False
        
        self.gridStatusBorder.Child = grid;
        
        grid.AddColumn().SetWidthToAuto()
        grid.AddColumn().SetWidthInPixels(5)
        grid.AddColumn().SetWidthToAuto()

        # Placing the text blocks on different rows of the grid
        # and placing data into the suitable rows and columns
        grid.AddRow()

        barIndexLabelTextBlock = TextBlock()
        barIndexLabelTextBlock.Text = "Bar Index"

        grid.AddChild(barIndexLabelTextBlock)

        self.barIndexTextBlock = TextBlock()

        grid.AddChild(self.barIndexTextBlock, 0, 2);
            
        grid.AddRow()

        priceLabelTextBlock = TextBlock()
        priceLabelTextBlock.Text = "Hover Price"

        grid.AddChild(priceLabelTextBlock, 1, 0)

        self.priceTextBlock = TextBlock()

        grid.AddChild(self.priceTextBlock, 1, 2);
        
        canvas = Canvas()
        canvas.AddChild(self.gridStatusBorder)
        
        api.Chart.AddControl(canvas)
            
        # Handling various mouse events
        api.Chart.MouseEnter += self.on_chart_mouse_enter
        api.Chart.MouseMove += self.on_chart_mouse_move
        api.Chart.MouseLeave += self.on_chart_mouse_leave

    def on_chart_mouse_enter(self, args):
        # Start displaying the border whenever the mouse cursor enters the chart
        self.gridStatusBorder.IsVisible = True

    def on_chart_mouse_move(self, args):
        # Moving the Border to match the position  of the mouse cursor
        self.gridStatusBorder.Top = args.MouseY
        self.gridStatusBorder.Left = args.MouseX
        # Updating the text inside the control on any mouse move
        self.barIndexTextBlock.Text = str(args.BarIndex)
        self.priceTextBlock.Text = str(api.Chart.YToYValue(args.MouseY))

    def on_chart_mouse_leave(self, args):
        # Hiding the border whenever the mouse cursor leaves the chart
        self.gridStatusBorder.IsVisible = False