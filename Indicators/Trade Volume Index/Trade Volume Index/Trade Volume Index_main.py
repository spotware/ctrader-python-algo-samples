import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from enum import Enum

class TradeVolumeIndex():
    def initialize(self):
        self.directions = IndicatorState(lambda : Direction.Accumulative)
        
    def calculate(self, index):
        if index == 0:
            api.Result[index] = 0
            return

        change = api.Source[index] - api.Source[index - 1]

        if change > api.Symbol.PipSize:
            self.directions.set_value(index, Direction.Accumulative)
        elif change < -api.Symbol.PipSize:
            self.directions.set_value(index, Direction.Distribute)
        else:
            self.directions.set_value(index, self.directions.get_value(index - 1))

        api.Result[index] = api.Result[index - 1]

        if self.directions.get_value(index) == Direction.Accumulative:
            api.Result[index] += api.Bars.TickVolumes[index]
        else:
            api.Result[index] -= api.Bars.TickVolumes[index]

class IndicatorState():
    def __init__(self, default_value_factory):
        self.default_value_factory = default_value_factory
        self.data = []
    
    def get_value(self, index):
        if index < 0:
            return self.default_value_factory()

        self.fill_with_default_values(index + 1)

        return self.data[index]

    def set_value(self, index, value):
        if index < 0:
            return

        self.fill_with_default_values(index + 1)

        self.data[index] = value

    def fill_with_default_values(self, index):
        while len(self.data) < index:
            self.data.append(self.default_value_factory())

class Direction(Enum):
    Accumulative=1
    Distribute=2