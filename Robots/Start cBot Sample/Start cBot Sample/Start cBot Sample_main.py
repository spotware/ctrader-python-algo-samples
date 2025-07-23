import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class StartcBotSample():
    def on_start(self):
        self.robot1 = api.Chart.Robots.Add("Sample Trend cBot", 0.01, MovingAverageType.Simple, api.Bars.ClosePrices, 10, 5)
        self.robot2 = api.Chart.Robots.Add("Sample Trend cBot", 0.01, MovingAverageType.Simple, api.Bars.ClosePrices, 12, 7)

        api.Chart.Robots.RobotStarted += self.on_chart_robots_started

    def on_chart_robots_started(self, args):
        api.Print(f"Robot Started: {args.Robot.Name}")

    def on_bar_closed(self):
        if self.robot1.State == RobotState.Stopped:
            self.robot1.Start()
            self.robot2.Stop()
        elif self.robot1.State == RobotState.Running:
            self.robot2.Start()
            self.robot1.Stop()