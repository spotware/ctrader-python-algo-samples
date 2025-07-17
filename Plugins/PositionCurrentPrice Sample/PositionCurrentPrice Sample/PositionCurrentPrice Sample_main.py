import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import TimeSpan

class PositionCurrentPriceSample():
    def on_start(self):
        self.selectedPosition = None
        # Configuring the new TextBlock
        self.currentPriceText = TextBlock()
        self.currentPriceText.Text = "Select a position above"
        self.currentPriceText.FontSize = 30
        self.currentPriceText.TextAlignment = TextAlignment.Center
        self.currentPriceText.FontWeight = FontWeight.ExtraBold
            
        # Adding a new ComboBox and adding existing positions as options
        self.positionSelectionComboBox = ComboBox()
            
        for position in api.Positions:
            self.positionSelectionComboBox.AddItem(str(position.Id))
            
        # Reacting to the selected position change
        self.positionSelectionComboBox.SelectedItemChanged += self.on_position_selection_comboBox_selected_item_changed;
            
        # Configuring the Grid where the ComboBox and the price TextBlock are placed
        blockGrid = Grid(2, 1)
        blockGrid.AddChild(self.positionSelectionComboBox, 0, 0)
        blockGrid.AddChild(self.currentPriceText, 1, 0)
            
        # Adding a new block into the ASP
        api.Asp.SymbolTab.AddBlock("Position.CurrentPrice").Child = blockGrid
                        
        # Starting the timer with 100 milliseconds as the tick
        api.Timer.Start(TimeSpan.FromMilliseconds(100))

    def on_timer(self):
        if self.selectedPosition is None:
            return
        self.currentPriceText.Text = str(self.selectedPosition.CurrentPrice)

    def on_position_selection_comboBox_selected_item_changed(self, args):
        self.selectedPosition = self.find_position_by_id(args.SelectedItem);

    def find_position_by_id(self, positionId):
        for position in api.Positions:
            if str(position.Id) == positionId:
                return position
        return null
