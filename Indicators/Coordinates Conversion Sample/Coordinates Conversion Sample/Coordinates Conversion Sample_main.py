import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CoordinatesConversionSample():
    def initialize(self):
        # Initialising the border and setting its parameters
        self.border = Border()
        self.border.BorderColor = Color.Gray
        self.border.BackgroundColor = Color.Gold
        self.border.BorderThickness = Thickness(3, 3, 3, 3)
        self.border.Padding = Thickness(5, 5, 5 , 5)
        self.border.CornerRadius = CornerRadius(5)
        self.border.Width = 80
        self.border.Height = 40

        # Initialising the TextBlock and setting its parameters
        self.barIndexTextBlock = TextBlock()
        self.barIndexTextBlock.Text = "..."
        self.barIndexTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        self.barIndexTextBlock.VerticalAlignment = VerticalAlignment.Center
            
        # Initialising the Canvas where the Border will be placed
        self.canvas = Canvas()
            
        # Adding controls as children
        self.border.Child = self.barIndexTextBlock
        self.canvas.AddChild(self.border);
            
        # Handling various mouse events
        api.Chart.MouseLeave += self.on_chart_mouse_leave
        api.Chart.MouseEnter += self.on_chart_mouse_enter
        api.Chart.MouseMove += self.on_chart_mouse_move
            
        # Showing the Canvas on the instance chart
        api.Chart.AddControl(self.canvas)

    def on_chart_mouse_leave(self, args):
        # Hiding the border when the cursor leaves  the chart
        self.border.IsVisible = False

    def on_chart_mouse_enter(self, args):
        # Showing the border when the cursor enters  the chart
        self.border.IsVisible = True

    def on_chart_mouse_move(self, args):
        # Moving the border together with the mouse cursor
        self.border.Left = args.MouseX
        self.border.Top = args.MouseY
            
        # Updating the text inside the TextBlock when the mouse cursor moves
        self.barIndexTextBlock.Text = str(api.Chart.XToBarIndex(args.MouseX))