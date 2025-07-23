import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class SmoothMouseMoveSample():
    def on_start(self):
        # Initialising the Border and setting  its parameters
        self.gridStatusBorder = Border()
        self.gridStatusBorder.IsHitTestVisible = False
        self.gridStatusBorder.CornerRadius = CornerRadius(3)
        self.gridStatusBorder.BorderThickness = Thickness(5)
        self.gridStatusBorder.Padding = Thickness(5)
        self.gridStatusBorder.Margin = Thickness(5, 5, 0, 0)
        self.gridStatusBorder.BackgroundColor = Color.Aqua
        self.gridStatusBorder.MaxHeight = 50
        self.gridStatusBorder.MaxWidth = 50

        # Initialising the TextBlock and making it so it displays whether grid display is on/off
        self.gridStatusTextBlock = TextBlock()
        self.gridStatusTextBlock.Text = str(api.Chart.DisplaySettings.Grid)

        # Placing controls inside one another and adding the Canvas to the Chart
        self.gridStatusBorder.Child = self.gridStatusTextBlock
        
        canvas = Canvas()
        canvas.AddChild(self.gridStatusBorder)
        
        api.Chart.AddControl(canvas)
            
        # Handling various mouse events
        api.Chart.MouseUp += self.on_chart_mouse_up
        api.Chart.MouseEnter += self.on_chart_mouse_enter
        api.Chart.MouseMove += self.on_chart_mouse_move
        api.Chart.MouseLeave += self.on_chart_mouse_leave

    def on_chart_mouse_up(self, args):
        # Setting the grid display on/off on mouse click
        api.Chart.DisplaySettings.Grid = False if api.Chart.DisplaySettings.Grid else True         
        # Updating the text inside the TextBlock
        self.gridStatusTextBlock.Text = str(api.Chart.DisplaySettings.Grid)

    def on_chart_mouse_enter(self, args):
        # Start displaying the border whenever the mouse cursor enters the chart
        self.gridStatusBorder.IsVisible = True

    def on_chart_mouse_move(self, args):
        # Moving the Border to match the position  of the mouse cursor
        self.gridStatusBorder.Top = args.MouseY
        self.gridStatusBorder.Left = args.MouseX

    def on_chart_mouse_leave(self, args):
        # Hiding the border whenever the mouse cursor leaves the chart
        self.gridStatusBorder.IsVisible = False
