import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class AlgoRegistrySample():
    def on_start(self):
        self.controlsGrid = Grid(2, 1)

        gridFirstRow = self.controlsGrid.Rows[0]
        gridFirstRow.SetHeightToAuto()

        gridSecondRow = self.controlsGrid.Rows[1]
        gridSecondRow.SetHeightInStars(1)

        self.cBotSelectionComboBox = ComboBox()

        for algo in api.AlgoRegistry:
            if algo.AlgoKind == AlgoKind.Robot:
                self.cBotSelectionComboBox.AddItem(algo.Name)
            
        self.cBotSelectionComboBox.SelectedItemChanged += self.on_cbot_selection_comboBox_selected_item_changed

        self.parametersInfoBlock = TextBlock()

        self.parametersInfoBlock.Margin = Thickness(0, 10, 20, 0)
        
        self.controlsGrid.AddChild(self.cBotSelectionComboBox, 0, 0)
        self.controlsGrid.AddChild(self.parametersInfoBlock, 1, 0)

        self.cBotManagementWindow = Window()
        self.cBotManagementWindow.Height = 300
        self.cBotManagementWindow.Width = 500
        self.cBotManagementWindow.Padding = Thickness(10, 10, 10 , 10)

        self.cBotManagementWindow.Child = self.controlsGrid
        self.cBotManagementWindow.Show()

    def on_cbot_selection_comboBox_selected_item_changed(self, args):
        self.selectedCBotName = args.SelectedItem;
        self.parametersInfoBlock.Text = self.get_parameters_info();

    def get_parameters_info(self):
        result = "";
            
        selectedCBot = RobotType(api.AlgoRegistry.Get(self.selectedCBotName, AlgoKind.Robot));

        for parameter in selectedCBot.Parameters:
            result += f"Param name: {parameter.Name} Param default value: {parameter.DefaultValue}\n";

        return result;

             
