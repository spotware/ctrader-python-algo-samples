import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class SmoothMouseMoveSample():
    def on_start(self):
        # Opening a new chart for GBPUSD and storing the Chart inside a varaible
        self.gpbusdChart = api.ChartManager.AddChartFrame("GBPUSD", TimeFrame.Minute2).Chart
            
        # Initialising the Border and setting its parameters
        self.ordersStatusBorder = Border()
        self.ordersStatusBorder.IsHitTestVisible = False
        self.ordersStatusBorder.CornerRadius = CornerRadius(3)
        self.ordersStatusBorder.BorderThickness = Thickness(1)
        self.ordersStatusBorder.Padding = Thickness(5)
        self.ordersStatusBorder.Margin = Thickness(5, 5, 0, 0)
        self.ordersStatusBorder.IsVisible = False

        # Initialising the TextBlock and settings its initial text
        self.ordersStatusTextBlock = TextBlock()
        self.ordersStatusTextBlock.Text = str(self.gpbusdChart.DisplaySettings.Orders)

        # Initialising the Canvas and placing the TextBlock inside it
        self.canvas = Canvas()
        self.canvas.AddChild(self.ordersStatusBorder)
            
        # Placing the TextBlock inside the Border
        self.ordersStatusBorder.Child = self.ordersStatusTextBlock

        # Adding the Canvas to the Chart
        self.gpbusdChart.AddControl(self.canvas);
            
        # Handling various mouse events
        self.gpbusdChart.MouseUp += self.on_chart_mouse_up
        self.gpbusdChart.MouseEnter += self.on_chart_mouse_enter
        self.gpbusdChart.MouseLeave += self.on_chart_mouse_leave
        self.gpbusdChart.MouseMove += self.on_chart_mouse_move

    def on_chart_mouse_up(self, args):
        # Enabling or disabling the displaying of orders on the chart
        self.gpbusdChart.DisplaySettings.Orders = True if self.gpbusdChart.DisplaySettings.Orders == False else False
            
        # Updating the text inside the TextBlock to match the current settings
        self.ordersStatusTextBlock.Text = str(self.gpbusdChart.DisplaySettings.Orders)

    def on_chart_mouse_enter(self, args):
        # Showing the border whenever the mouse cursor enters the chart
        self.ordersStatusBorder.IsVisible = True

    def on_chart_mouse_leave(self, args):
        # Hiding the border whenever the  mouse cursor leaves the chart
        self.ordersStatusBorder.IsVisible = False

    def on_chart_mouse_move(self, args):
        # Moving the border to follow the mouse cursor
        self.ordersStatusBorder.Top = args.MouseY;
        self.ordersStatusBorder.Left = args.MouseX;