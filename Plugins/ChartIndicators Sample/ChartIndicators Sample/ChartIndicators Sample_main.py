import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartIndicatorsSample():
    def on_start(self):
        aspTab = api.Asp.AddTab("Chart Indicators")
            
        self.chartIndicatorsControl = ChartIndicatorsControl(api.AlgoRegistry)
        self.chartIndicatorsControl.content.VerticalAlignment = VerticalAlignment.Top

        aspTab.Child = self.chartIndicatorsControl.content

        self.set_control_chart()

        api.ChartManager.ActiveFrameChanged += lambda _ : self.set_control_chart()
        
    def set_control_chart(self):
        if api.ChartManager.ActiveFrame is None or isinstance(api.ChartManager.ActiveFrame.__implementation__, ChartFrame) == False:
                return;

        chartFrame = ChartFrame(api.ChartManager.ActiveFrame)
        self.chartIndicatorsControl.setChart(chartFrame.Chart)

class ChartIndicatorsControl():
    def __init__(self, algoRegistry):
        self.algoRegistry = algoRegistry
        self.chart = None
        
        self.content = Grid(6, 2)
        
        self.content.AddChild(self.get_text_block("Indicators #"), 0, 0)

        self.indicatorsCountTextBlock = self.get_text_block()
        
        self.content.AddChild(self.indicatorsCountTextBlock, 0, 1)

        self.content.AddChild(self.get_text_block("Indicators"), 1, 0)

        self.indicatorsTextBlock = self.get_text_block()
        
        self.content.AddChild(self.indicatorsTextBlock, 1, 1)

        self.indicatorTypesComboBox = ComboBox()
        self.indicatorTypesComboBox.Margin = Thickness(3)
        self.indicatorTypesComboBox.FontSize = 16
        self.indicatorTypesComboBox.FontWeight = FontWeight.Bold
        self.indicatorTypesComboBox.FontFamily = "Calibri"

        self.populate_types()

        self.addIndicatorButton = Button()
        self.addIndicatorButton.Text = "Add Indicator"
        self.addIndicatorButton.Margin = Thickness(3)
        self.addIndicatorButton.FontSize = 16
        self.addIndicatorButton.FontWeight = FontWeight.Bold
        self.addIndicatorButton.FontFamily = "Calibri"

        self.addIndicatorButton.Click += self.on_add_indicator_button_click
        
        addIndicatorPanel = StackPanel()
        addIndicatorPanel.Orientation = Orientation.Horizontal

        addIndicatorPanel.AddChild(self.indicatorTypesComboBox)
        addIndicatorPanel.AddChild(self.addIndicatorButton)

        self.content.AddChild(addIndicatorPanel, 2, 0, 1, 2)

        self.removeIndicatorsButton = Button()
        self.removeIndicatorsButton.Text = "Remove All Indicators"
        self.removeIndicatorsButton.Margin = Thickness(3)
        self.removeIndicatorsButton.FontSize = 16
        self.removeIndicatorsButton.FontWeight = FontWeight.Bold
        self.removeIndicatorsButton.FontFamily = "Calibri"

        self.removeIndicatorsButton.Click += self.on_remove_indicators_button_click
        
        self.content.AddChild(self.removeIndicatorsButton, 3, 0, 1, 2)
        
        self.algoRegistry.AlgoTypeInstalled += lambda _ : self.populate_types()
        self.algoRegistry.AlgoTypeDeleted += lambda _ : self.populate_types()

    def setChart(self, chart):
        if self.chart == chart:
            return

        previousChart = self.chart
        self.chart = chart

        self.update_status()
        
        chart.Indicators.IndicatorAdded += self.on_indicators_added
        chart.Indicators.IndicatorRemoved += self.on_indicators_removed
        
        if previousChart is None:
            return
        
        previousChart.Indicators.IndicatorAdded -= self.on_indicators_added
        previousChart.Indicators.IndicatorRemoved -= self.on_indicators_removed

    def on_indicators_added(self, args):
        self.update_status()

    def on_indicators_removed(self, args):
        self.update_status()

    def on_remove_indicators_button_click(self, args):
        for chartIndicator in self.chart.Indicators:
            self.chart.Indicators.Remove(chartIndicator)

    def on_add_indicator_button_click(self, args):
        indicatorType = self.algoRegistry.Get(self.indicatorTypesComboBox.SelectedItem)

        if indicatorType.AlgoKind != AlgoKind.CustomIndicator and indicatorType.AlgoKind != AlgoKind.StandardIndicator:
            return

        self.chart.Indicators.Add(indicatorType.Name)

    def update_status(self):
        self.indicatorsCountTextBlock.Text = str(self.chart.Indicators.Count)
        self.indicatorsTextBlock.Text = ", ".join([i.Name for i in self.chart.Indicators])

    def populate_types(self):
        for algoType in self.algoRegistry:
            if algoType.AlgoKind != AlgoKind.CustomIndicator and algoType.AlgoKind != AlgoKind.StandardIndicator:
                continue            

            self.indicatorTypesComboBox.AddItem(algoType.Name)
            self.indicatorTypesComboBox.SelectedItem = algoType.Name
    
    def get_text_block(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 16
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock