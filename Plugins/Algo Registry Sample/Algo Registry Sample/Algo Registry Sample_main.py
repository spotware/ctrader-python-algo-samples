import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AlgoRegistrySample():
    def on_start(self):
        tradeWatchTab = api.TradeWatch.AddTab("Algo Registry")

        panel = StackPanel()
        panel.Orientation = Orientation.Horizontal
        panel.HorizontalAlignment = HorizontalAlignment.Center

        algoStateControl = AlgoStatsControl(api.AlgoRegistry)
        algoStateControl.Margin = 10
        algoStateControl.VerticalAlignment = VerticalAlignment.Top

        panel.AddChild(algoStateControl.content)

        algoTypeInfoControl = AlgoTypeInfoControl(api.AlgoRegistry)
        algoTypeInfoControl.Margin = 10
        algoTypeInfoControl.VerticalAlignment = VerticalAlignment.Top

        panel.AddChild(algoTypeInfoControl.content)

        tradeWatchTab.Child = panel

class AlgoStatsControl:
    def __init__(self, algoRegistry):
        self.algoRegistry = algoRegistry
        
        self.content = Grid(6, 2)

        titleTextBlock = self.GetTextBlock("Algo Stats")

        titleTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        
        self.content.AddChild(titleTextBlock, 0, 0, 1, 2)
  
        self.content.AddChild(self.GetTextBlock("Algos #"), 1, 0)

        self.algosCountTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.algosCountTextBlock, 1, 1)

        self.content.AddChild(self.GetTextBlock("Standard Indicators #"), 2, 0)

        self.standardIndicatorsCountTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.standardIndicatorsCountTextBlock, 2, 1)
        
        self.content.AddChild(self.GetTextBlock("Custom Indicators #"), 3, 0)

        self.customIndicatorsCountTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.customIndicatorsCountTextBlock, 3, 1)
        
        self.content.AddChild(self.GetTextBlock("cBots #"), 4, 0)

        self.botsCountTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.botsCountTextBlock, 4, 1)
        
        self.content.AddChild(self.GetTextBlock("Plugins #"), 5, 0)

        self.pluginsCountTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.pluginsCountTextBlock, 5, 1)
        
        self.Populate()
        
        self.algoRegistry.AlgoTypeInstalled += lambda _ : self.Populate()
        self.algoRegistry.AlgoTypeDeleted += lambda _ : self.Populate()

    def Populate(self): 
        self.algosCountTextBlock.Text = str(self.algoRegistry.Count)
        self.botsCountTextBlock.Text = str(len([t for t in self.algoRegistry if t.AlgoKind == AlgoKind.Robot]))
        self.customIndicatorsCountTextBlock.Text = str(len([t for t in self.algoRegistry if t.AlgoKind == AlgoKind.CustomIndicator]))
        self.standardIndicatorsCountTextBlock.Text =  str(len([t for t in self.algoRegistry if t.AlgoKind == AlgoKind.StandardIndicator]))
        self.pluginsCountTextBlock.Text = str(len([t for t in self.algoRegistry if t.AlgoKind == AlgoKind.Plugin]))

    def GetTextBlock(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 20
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock

class AlgoTypeInfoControl():
    def __init__(self, algoRegistry):
        self.algoRegistry = algoRegistry
        self.content = Grid(5, 2)
        self.content.BackgroundColor = Color.Gray

        titleTextBlock = self.GetTextBlock("Algo Type Info")
        
        titleTextBlock.HorizontalAlignment = HorizontalAlignment.Center
        
        self.content.AddChild(titleTextBlock, 0, 0, 1, 2)
        
        self.content.AddChild(self.GetTextBlock("Types"), 1, 0)

        self.algoTypesComboBox = ComboBox()
        self.algoTypesComboBox.Margin = Thickness(3)
        self.algoTypesComboBox.FontSize = 20
        self.algoTypesComboBox.FontWeight = FontWeight.Bold
        self.algoTypesComboBox.FontFamily = "Calibri"
        self.algoTypesComboBox.Padding = Thickness(2)
        
        self.content.AddChild(self.algoTypesComboBox, 1, 1)
        self.content.AddChild(self.GetTextBlock("Kind"), 2, 0)

        self.algoTypeKindTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.algoTypeKindTextBlock, 2, 1) 
        self.content.AddChild(self.GetTextBlock("Parameters"), 3, 0)

        self.algoTypeParametersTextBlock = self.GetTextBlock()
  
        self.content.AddChild(self.algoTypeParametersTextBlock, 3, 1)
        self.content.AddChild(self.GetTextBlock("Outputs"), 4, 0)

        self.algoTypeOutputsTextBlock = self.GetTextBlock()
        
        self.content.AddChild(self.algoTypeOutputsTextBlock, 4, 1);
        
        self.algoTypesComboBox.SelectedItemChanged += self.on_algo_types_combo_box_selected_item_changed
        
        self.populate_types()

        self.algoRegistry.AlgoTypeInstalled += lambda _ : self.populate_types()
        self.algoRegistry.AlgoTypeDeleted += lambda _ : self.populate_types()

    def on_algo_types_combo_box_selected_item_changed(self, args):
        algoType = self.algoRegistry.Get(self.algoTypesComboBox.SelectedItem)
        if algoType is None:
            self.algoTypeKindTextBlock.Text = None
            self.algoTypeParametersTextBlock.Text = None
            self.algoTypeOutputsTextBlock.Text = None 
            return

        self.algoTypeKindTextBlock.Text = str(algoType.AlgoKind)

        if isinstance(algoType.__implementation__, IndicatorType):
            indicatorType = IndicatorType(algoType)
            self.algoTypeParametersTextBlock.Text = ", ".join([p.Name for p in indicatorType.Parameters])
            self.algoTypeOutputsTextBlock.Text = ", ".join([o.Name for o in indicatorType.Outputs])
        elif isinstance(algoType.__implementation__, RobotType):
            robotType = RobotType(algoType)
            self.algoTypeParametersTextBlock.Text = ", ".join([p.Name for p in robotType.Parameters])
            self.algoTypeOutputsTextBlock.Text = None
        else:
            self.algoTypeParametersTextBlock.Text = None
            self.algoTypeOutputsTextBlock.Text = None

    def populate_types(self):

        for algoType in self.algoRegistry:
            self.algoTypesComboBox.AddItem(algoType.Name)
        
        firstAlgoType= next(iter(self.algoRegistry), None)
        self.algoTypesComboBox.SelectedItem = firstAlgoType.Name if firstAlgoType is not None else None;

        self.on_algo_types_combo_box_selected_item_changed(None);

    def GetTextBlock(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 20
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock
