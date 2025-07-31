import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CustomControlSample():
    def initialize(self):
        comboBox = CustomComboBox()
        comboBox.content.HorizontalAlignment = HorizontalAlignment.Center
        comboBox.content.VerticalAlignment = VerticalAlignment.Center

        comboBox.items.append("Item 1")
        comboBox.items.append("Item 2")
        comboBox.items.append("Item 3")
        comboBox.items.append("Item 4")
        comboBox.items.append("Item 5")

        api.Chart.AddControl(comboBox.content)

class CustomComboBox():
    def __init__(self):
        self.items = []
        self.is_expanded = False
        self.textBox = TextBox()
        self.textBox.Width = 100
        self.textBox.IsReadOnly = True
        self.textBox.IsReadOnlyCaretVisible = False

        self.button = Button()
        self.button.Text = "▼"
        self.button.Click += self.on_button_click

        stackPanel = StackPanel()
        stackPanel.Orientation = Orientation.Horizontal

        stackPanel.AddChild(self.textBox)
        stackPanel.AddChild(self.button)

        self.content = StackPanel()
        self.content.Orientation = Orientation.Vertical

        self.content.AddChild(stackPanel)

    def on_button_click(self, args):
        if hasattr(self, "itemsGrid") and self.itemsGrid is not None:
            self.content.RemoveChild(self.itemsGrid)

        if self.is_expanded:
            self.is_expanded = False
            return

        self.is_expanded = True

        self.itemsGrid = Grid(len(self.items), 1)
        
        for i in range(len(self.items)):
            item = self.items[i]
            textBlock = TextBlock()
            textBlock.Text = str(item)
            self.itemsGrid.AddChild(textBlock, i, 0)

        self.content.AddChild(self.itemsGrid)