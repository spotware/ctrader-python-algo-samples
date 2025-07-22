import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionEventsSample():
    def on_start(self):
        api.Positions.Opened += self.on_position_opened
        api.Positions.Closed += self.on_position_closed
        api.Positions.Modified += self.on_position_modified

    def on_position_opened(self, args):
        openedPosition = args.Position
        api.Print(f"Opened Postion Id: {openedPosition.Id}")

    def on_position_closed(self, args):
        closedPosition = args.Position
        api.Print(f"Closed Postion Id: {closedPosition.Id} | Reason: {args.Reason}")

    def on_position_modified(self, args):
        modifiedPosition = args.Position
        api.Print(f"Modified Postion Id: {modifiedPosition.Id}")
