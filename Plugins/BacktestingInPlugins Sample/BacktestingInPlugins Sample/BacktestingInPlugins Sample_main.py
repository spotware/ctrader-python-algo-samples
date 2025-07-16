import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

from System import DateTime
from System.Text.Json.Nodes import JsonNode
from System.Text.Json import JsonDocumentOptions
import json

class BacktestingInPluginsSample():
    def on_start(self):
        self.grid = Grid(3, 1)
        
        self.cBotsComboBox = ComboBox()

        self.startBacktestingButton = Button()
        self.startBacktestingButton.BackgroundColor = Color.Green
        self.startBacktestingButton.CornerRadius = CornerRadius(5)
        self.startBacktestingButton.Text = "Start Backtesting"

        self.resultsTextBlock = TextBlock()
        self.resultsTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        self.resultsTextBlock.VerticalAlignment = VerticalAlignment.Center
        self.resultsTextBlock.Text = "Select a cBot..."

        self.grid.AddChild(self.cBotsComboBox, 0, 0)
        self.grid.AddChild(self.startBacktestingButton, 1, 0)
        self.grid.AddChild(self.resultsTextBlock, 2, 0)
           
        block = api.Asp.SymbolTab.AddBlock("Backtesting Plugin")
        block.Child = self.grid
            
        # Populating the ComboBox with existing cBots
        self.populate_cbots_combobox();

        self.startBacktestingButton.Click += self.on_start_backtesting_button_click;
        self.cBotsComboBox.SelectedItemChanged += self.on_cbots_combobox_selected_item_changed;
        api.Backtesting.Completed += self.on_backtesting_completed;

    def populate_cbots_combobox(self):
        # Iterating over the AlgoRegistry and getting the names of all installed cBots
        for robotType in api.AlgoRegistry.Robots:
            self.cBotsComboBox.AddItem(robotType.Name)

    def on_start_backtesting_button_click(self, args):
        backtestingSettings = BacktestingSettings()
        backtestingSettings.DataMode = BacktestingDataMode.M1
        backtestingSettings.StartTimeUtc = DateTime(DateTime.UtcNow.Year - 1, DateTime.UtcNow.Month, DateTime.UtcNow.Day)
        backtestingSettings.EndTimeUtc = DateTime.UtcNow
        backtestingSettings.Balance = 10000
            
        # Starting backtesting on EURUSD h1
        self.backtestingProcess = api.Backtesting.Start(self.selectedRobotType, "EURUSD", TimeFrame.Hour, backtestingSettings)
            
        # Disabling other controls and changing the text inside the TextBlock
        self.cBotsComboBox.IsEnabled = False
        self.startBacktestingButton.IsEnabled = False
        self.resultsTextBlock.Text = "Backtesting in progress..."

    def on_cbots_combobox_selected_item_changed(self, args):
        self.selectedRobotType = RobotType(api.AlgoRegistry.Get(args.SelectedItem))

    def on_backtesting_completed(self, args):
        if int(args.Process.BacktestingError) == 0:
            api.Print(f"Backtesting failed with error {args.Process.BacktestingError}")
            return
            
        jsonResults = json.loads(args.JsonReport)
            
        # # Attaining the ROI and net profit from backtesting results
        self.resultsTextBlock.Text = f"ROI: {jsonResults["main"]["roi"]}\nNet Profit: {jsonResults["main"]["netProfit"]}"
            
        # Re-enabling controls after backteting is finished
        self.cBotsComboBox.IsEnabled = True;
        self.startBacktestingButton.IsEnabled = True;
