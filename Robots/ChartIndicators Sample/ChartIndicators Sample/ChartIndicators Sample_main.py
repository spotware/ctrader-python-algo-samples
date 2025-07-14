import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class ChartIndicatorsSample():
    def on_start(self):
        self.indicatorSelectionComboBox = ComboBox()
        for indicator in api.ChartIndicators:
            self.indicatorSelectionComboBox.AddItem(f"{indicator.Name} / {indicator.InstanceId}")
        # Handling the SelectedItemChanged event
        self.indicatorSelectionComboBox.SelectedItemChanged += self.on_indicator_selection_comboBox_selected_item_changed
        # Initialising the indicator removal button
        self.removeIndicatorButton = Button()
        self.removeIndicatorButton.BackgroundColor = Color.Indigo
        self.removeIndicatorButton.Text = "Remove Selected Indicator"
        # Handling the Click event for the button
        self.removeIndicatorButton.Click += self.on_remove_indicator_button_click 
        # Initialising the Grid to be used for storing other controls
        self.windowGrid = Grid(2, 1)
        self.windowGrid.AddChild(self.indicatorSelectionComboBox, 0, 0)
        self.windowGrid.AddChild(self.removeIndicatorButton, 1, 0)
        # Initialising the detached window and adding the Grid as its child
        self.indicatorRemovalWindow = Window()
        self.indicatorRemovalWindow.Padding = Thickness(10, 10, 10, 10)
        self.indicatorRemovalWindow.MaxHeight = 200
        self.indicatorRemovalWindow.MaxWidth = 500
        self.indicatorRemovalWindow.Child = self.windowGrid
        # Showing the window on cBot start
        self.indicatorRemovalWindow.Show()

    def on_indicator_selection_comboBox_selected_item_changed(self, args):
        # Recovering the instanceId from the selected item and storing the found ChartIndicator
        instanceId = args.SelectedItem.split(" / ")
        self.selectedIndicator = api.ChartIndicators[instanceId[1]]

    def on_remove_indicator_button_click(self, args):
        # Removing the currently selected ChartIndicator on button click
        api.ChartIndicators.Remove(self.selectedIndicator)