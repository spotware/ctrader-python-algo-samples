import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class VerticalAlignmentSample():
    def initialize(self):
        textBlock = TextBlock()
        textBlock.Text = f"Alignment: {api.VerticalAlignment}"
        textBlock.HorizontalAlignment = HorizontalAlignment.Center
        textBlock.VerticalAlignment = api.VerticalAlignment

        api.Chart.AddControl(textBlock);