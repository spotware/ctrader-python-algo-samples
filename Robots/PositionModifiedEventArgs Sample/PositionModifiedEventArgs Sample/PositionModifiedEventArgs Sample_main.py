import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionModifiedEventArgsSample():
    def on_start(self):
        api.Positions.Modified += self.on_positions_modified

    def on_positions_modified(self, args):
        api.Print(f"Position {args.Position.Id} modified")