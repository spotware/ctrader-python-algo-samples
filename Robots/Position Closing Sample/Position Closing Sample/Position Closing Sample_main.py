import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class PositionClosingSample():
    def on_start(self):
        positions = []

        if len(api.PositionComment) > 0 and len(api.PositionLabel) > 0:
            positions = [position for position in api.Positions.FindAll(api.PositionLabel) if position.Comment == api.PositionComment]
        elif len(api.PositionComment) > 0:
            positions = [position for position in api.Positions if position.Comment == api.PositionComment]
        elif len(api.PositionLabel) > 0:
            positions = [position for position in api.Positions.FindAll(api.PositionLabel)]

        if len(positions) == 0:
            api.Print("Couldn't find matching postions, please check the comment and label")
        else:
            for position in positions:
                api.ClosePosition(position)

        api.Stop()