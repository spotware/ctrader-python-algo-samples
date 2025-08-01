import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class HorizontalAlignmentSample():
    def initialize(self):
        textBlock = TextBlock()
        textBlock.Text = f"Alignment: {api.HorizontalAlignment}"
        textBlock.HorizontalAlignment = api.HorizontalAlignment
        textBlock.VerticalAlignment = VerticalAlignment.Center

        api.Chart.AddControl(textBlock);