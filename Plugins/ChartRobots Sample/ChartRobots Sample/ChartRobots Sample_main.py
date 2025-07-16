import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartRobotsSample():
    def on_start(self):
        aspTab = api.Asp.AddTab("Chart Robots")
            
        self.chartRobotsControl = ChartRobotsControl(api.AlgoRegistry)
        self.chartRobotsControl.content.VerticalAlignment = VerticalAlignment.Top

        aspTab.Child = self.chartRobotsControl.content

        self.set_control_chart()

        api.ChartManager.ActiveFrameChanged += lambda _ : self.set_control_chart()
        
    def set_control_chart(self):
        if api.ChartManager.ActiveFrame is None or isinstance(api.ChartManager.ActiveFrame.__implementation__, ChartFrame) == False:
                return;

        chartFrame = ChartFrame(api.ChartManager.ActiveFrame)
        self.chartRobotsControl.setChart(chartFrame.Chart)

class ChartRobotsControl():
    def __init__(self, algoRegistry):
        self.algoRegistry = algoRegistry
        self.chart = None
        
        self.content = Grid(7, 2)
        
        self.content.AddChild(self.get_text_block("Robots #"), 0, 0)

        self.robotsCountTextBlock = self.get_text_block()
        
        self.content.AddChild(self.robotsCountTextBlock, 0, 1)

        self.content.AddChild(self.get_text_block("Running Robots #"), 1, 0);

        self.runningRobotsCountTextBlock = self.get_text_block();
        
        self.content.AddChild(self.runningRobotsCountTextBlock, 1, 1);

        self.content.AddChild(self.get_text_block("Robots"), 2, 0)

        self.robotsTextBlock = self.get_text_block()
        
        self.content.AddChild(self.robotsTextBlock, 2, 1)

        self.robotTypesComboBox = ComboBox()
        self.robotTypesComboBox.Margin = Thickness(3)
        self.robotTypesComboBox.FontSize = 16
        self.robotTypesComboBox.FontWeight = FontWeight.Bold
        self.robotTypesComboBox.FontFamily = "Calibri"

        self.populate_types()

        self.addRobotButton = Button()
        self.addRobotButton.Text = "Add Robot"
        self.addRobotButton.Margin = Thickness(3)
        self.addRobotButton.FontSize = 16
        self.addRobotButton.FontWeight = FontWeight.Bold
        self.addRobotButton.FontFamily = "Calibri"

        self.addRobotButton.Click += self.on_add_robot_button_click
        
        addRobotPanel = StackPanel()
        addRobotPanel.Orientation = Orientation.Horizontal

        addRobotPanel.AddChild(self.robotTypesComboBox)
        addRobotPanel.AddChild(self.addRobotButton)

        self.content.AddChild(addRobotPanel, 3, 0, 1, 2)

        self.removeRobotsButton = Button()
        self.removeRobotsButton.Text = "Remove All Robots"
        self.removeRobotsButton.Margin = Thickness(3)
        self.removeRobotsButton.FontSize = 16
        self.removeRobotsButton.FontWeight = FontWeight.Bold
        self.removeRobotsButton.FontFamily = "Calibri"

        self.removeRobotsButton.Click += self.on_remove_robots_button_click
        
        self.content.AddChild(self.removeRobotsButton, 4, 0, 1, 2)
        
        self.startRobotsButton = Button()
        self.startRobotsButton.Text = "Start All Robots"
        self.startRobotsButton.Margin = Thickness(3)
        self.startRobotsButton.FontSize = 16
        self.startRobotsButton.FontWeight = FontWeight.Bold
        self.startRobotsButton.FontFamily = "Calibri"

        self.startRobotsButton.Click += self.on_start_robots_button_click
        
        self.content.AddChild(self.startRobotsButton, 5, 0, 1, 2)

        self.stopRobotsButton = Button()
        self.stopRobotsButton.Text = "Stop All Robots"
        self.stopRobotsButton.Margin = Thickness(3)
        self.stopRobotsButton.FontSize = 16
        self.stopRobotsButton.FontWeight = FontWeight.Bold
        self.stopRobotsButton.FontFamily = "Calibri"

        self.stopRobotsButton.Click += self.on_stop_robots_button_click
        
        self.content.AddChild(self.stopRobotsButton, 6, 0, 1, 2)

        self.algoRegistry.AlgoTypeInstalled += lambda _ : self.populate_types()
        self.algoRegistry.AlgoTypeDeleted += lambda _ : self.populate_types()

    def setChart(self, chart):
        if self.chart == chart:
            return

        previousChart = self.chart
        self.chart = chart

        self.update_status()
        
        chart.Robots.RobotAdded += self.on_robots_added
        chart.Robots.RobotRemoved += self.on_robots_removed
        chart.Robots.RobotStarted += self.on_robots_started
        chart.Robots.RobotStopped += self.on_robots_stopped

        if previousChart is None:
            return
        
        previousChart.Robots.RobotAdded -= self.on_robots_added
        previousChart.Robots.RobotRemoved -= self.on_robots_removed
        previousChart.Robots.RobotStarted -= self.on_robots_started
        previousChart.Robots.RobotStopped -= self.on_robots_stopped

    def on_robots_added(self, args):
        self.update_status()

    def on_robots_removed(self, args):
        self.update_status()

    def on_robots_started(self, args):
        self.update_status()

    def on_robots_stopped(self, args):
        self.update_status()

    def on_remove_robots_button_click(self, args):
        for chartRobot in self.chart.Robots:
            self.chart.Robots.Remove(chartRobot)

    def on_start_robots_button_click(self, args):
        for chartRobot in self.chart.Robots:
            if chartRobot.State == RobotState.Running or chartRobot.State == RobotState.Restarting:
                continue

            chartRobot.Start()

    def on_stop_robots_button_click(self, args):
        for chartRobot in self.chart.Robots:
            if chartRobot.State == RobotState.Stopped or chartRobot.State == RobotState.Stopping:
                continue

            chartRobot.Stop()

    def on_add_robot_button_click(self, args):
        robotType = self.algoRegistry.Get(self.robotTypesComboBox.SelectedItem)

        if robotType.AlgoKind != AlgoKind.Robot:
            return

        self.chart.Robots.Add(robotType.Name)

    def update_status(self):
        self.robotsCountTextBlock.Text = str(self.chart.Robots.Count)
        self.robotsTextBlock.Text = ", ".join([i.Name for i in self.chart.Robots])
        self.runningRobotsCountTextBlock.Text = str(len([r for r in self.chart.Robots if r.State == RobotState.Running]))

    def populate_types(self):
        for algoType in self.algoRegistry:
            if algoType.AlgoKind != AlgoKind.Robot:
                continue            

            self.robotTypesComboBox.AddItem(algoType.Name)
            self.robotTypesComboBox.SelectedItem = algoType.Name
    
    def get_text_block(self, text = None):
        textBlock = TextBlock()
        textBlock.Margin = Thickness(3)
        textBlock.FontSize = 16
        textBlock.FontWeight = FontWeight.Bold
        textBlock.FontFamily = "Calibri"
        textBlock.Text = text
        return textBlock