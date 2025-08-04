import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class LineStackingStrategySample():
    def initialize(self):
        stackPanel = StackPanel()
        stackPanel.Orientation = Orientation.Vertical
        stackPanel.BackgroundColor = Color.Gold
        stackPanel.Opacity = 0.6
        stackPanel.HorizontalAlignment = HorizontalAlignment.Center
        stackPanel.VerticalAlignment = VerticalAlignment.Center

        text = """First line of text
Second line of text
Third line of text
Fourth line of text
Fifth line of text"""

        blockLineHeightTextBlock = TextBlock()
        blockLineHeightTextBlock.Margin = Thickness(5)
        blockLineHeightTextBlock.Text =  f"LineStackingStrategy = BlockLineHeight:\n{text}"
        blockLineHeightTextBlock.LineStackingStrategy = LineStackingStrategy.BlockLineHeight
        blockLineHeightTextBlock.FontWeight = FontWeight.Bold
        blockLineHeightTextBlock.ForegroundColor = Color.Black

        stackPanel.AddChild(blockLineHeightTextBlock)

        maxHeightTextBlock = TextBlock()
        maxHeightTextBlock.Margin = Thickness(5)
        maxHeightTextBlock.Text =  f"LineStackingStrategy = MaxHeight:\n{text}"
        maxHeightTextBlock.LineStackingStrategy = LineStackingStrategy.MaxHeight
        maxHeightTextBlock.FontWeight = FontWeight.Bold
        maxHeightTextBlock.ForegroundColor = Color.Black

        stackPanel.AddChild(maxHeightTextBlock);

        api.Chart.AddControl(stackPanel);