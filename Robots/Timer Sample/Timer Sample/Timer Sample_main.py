import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *
from System import TimeSpan

# Import trading wrapper functions
from robot_wrapper import *

class TimerSample():
    def on_start(self):
        # You can use on_timer method to listen to timer ticks
        # or you can also use the TimerTick event instead of OnTimer method
        api.Timer.TimerTick += self.on_timer_tick
        # You have to call timer start method with interval either in seconds or TimeSpan
        # api.Timer.Start(3)
        api.Timer.Start(TimeSpan.FromSeconds(3))

    def on_timer(self):
        api.Print("on_timer")
        api.Timer.Stop()

    def on_timer_tick(self):
        api.Print("on_timer_tick")