import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartKeyDownSample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.Orientation = Orientation.Vertical
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.7
        stackPanel.Width = 200

        keyDownHandlerTextBlock = TextBlock()
        keyDownHandlerTextBlock.Text = "Key Down Handler"
        keyDownHandlerTextBlock.FontWeight = FontWeight.ExtraBold
        keyDownHandlerTextBlock.Margin = Thickness(5)
        keyDownHandlerTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        keyDownHandlerTextBlock.ForegroundColor = Color.Black
        
        stackPanel.AddChild(keyDownHandlerTextBlock)

        grid = Grid(2, 2)

        keyDownLabelTextBlock = TextBlock()
        keyDownLabelTextBlock.Text = "Key Down"
        keyDownLabelTextBlock.Margin = Thickness(5)
        keyDownLabelTextBlock.ForegroundColor = Color.Black

        grid.AddChild(keyDownLabelTextBlock, 0, 0)

        self.keyDownTextBlock = TextBlock()
        self.keyDownTextBlock.Margin = Thickness(5)
        self.keyDownTextBlock.ForegroundColor = Color.Black

        grid.AddChild(self.keyDownTextBlock, 0, 1)

        keyCombinationLabelTextBlock = TextBlock()
        keyCombinationLabelTextBlock.Text = "Key Combination"
        keyCombinationLabelTextBlock.Margin = Thickness(5)
        keyCombinationLabelTextBlock.ForegroundColor = Color.Black

        grid.AddChild(keyCombinationLabelTextBlock, 1, 0)

        self.keyCombinationTextBlock = TextBlock()
        self.keyCombinationTextBlock.Margin = Thickness(5)
        self.keyCombinationTextBlock.ForegroundColor = Color.Black

        grid.AddChild(self.keyCombinationTextBlock, 1, 1)

        stackPanel.AddChild(grid)

        api.Chart.AddControl(stackPanel)
        api.Chart.KeyDown += self.on_chart_key_down

    def on_chart_key_down(self, args):
        self.keyDownTextBlock.Text = str(args.Key)
        self.keyCombinationTextBlock.Text = ""
            
        if args.AltKey:
            self.keyCombinationTextBlock.Text += f"{self.keyCombinationTextBlock.Text}Alt, "
        if args.ShiftKey:
            self.keyCombinationTextBlock.Text += f"{self.keyCombinationTextBlock.Text}Shift, "
        if args.CtrlKey:
            self.keyCombinationTextBlock.Text += f"{self.keyCombinationTextBlock.Text}Ctrl, "