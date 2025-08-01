import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import Action

class KeySample():
    def initialize(self):
        api.Chart.MouseMove += self.on_chart_mouse_move
        api.Chart.MouseEnter += lambda _: self.reset_mouse_location()
        api.Chart.MouseLeave += lambda _: self.reset_mouse_location()

        self.reset_mouse_location()

        api.Chart.AddHotkey(Action(self.draw_lines), api.HotKey)

    def reset_mouse_location(self):
        self.mouseBarIndex = -1
        self.mousePrice = None

    def on_chart_mouse_move(self, args):
        self.mouseBarIndex = args.BarIndex
        self.mousePrice = args.YValue

    def draw_lines(self):
        if self.mouseBarIndex == -1 or self.mousePrice is None:
            return

        api.Chart.DrawVerticalLine(str(self.mouseBarIndex), int(self.mouseBarIndex), Color.Red)
        api.Chart.DrawHorizontalLine(str(self.mousePrice), self.mousePrice, Color.Red)