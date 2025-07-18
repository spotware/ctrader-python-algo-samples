import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

class GetFitnessArgsSample():
    def get_fitness(self, args):
        # Here we are using the win rate as fitness
        # You can use any other value by combining the values of GetFitnessArgs object properties
        return args.WinningTrades / args.TotalTrades