import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class ParabolicSAR():
    def initialize(self):
        self.states = IndicatorState(lambda : SarIndexState())
        
    def calculate(self, index):
        currentHigh = api.Bars.HighPrices[index]
        currentLow = api.Bars.LowPrices[index]

        previousHigh = api.Bars.HighPrices[index - 1]
        previousLow = api.Bars.LowPrices[index - 1]

        if index == 1:
            isUpTrend = currentHigh > previousHigh and currentLow > previousLow
            if isUpTrend:
                self.setup_initial_value(index, previousLow, true, previousHigh)
            else:
                self.setup_initial_value(index, previousHigh, False, previousLow)

        currentSar = self.calculate_current_sar(index)
        previousState = self.states.get_value(index - 1)
        currentState = self.states.get_value(index)

        self.copy_state(previousState, currentState)

        if previousState.is_up_trend:
            currentSar = self.get_min([currentSar, api.Bars.LowPrices[index - 1], api.Bars.LowPrices[index - 2]])

            if currentSar > currentLow:
                currentState.is_up_trend = False
                currentSar = previousState.extreme_point
                currentState.acceleration_factor = api.MinAf
                currentState.extreme_point = currentLow
            elif currentHigh > previousState.extreme_point:
                currentState.extreme_point = currentHigh
                currentState.acceleration_factor = self.increase_acceleration_factor(previousState.acceleration_factor)
        else:
            currentSar = self.get_max([currentSar, api.Bars.HighPrices[index - 1], api.Bars.HighPrices[index - 2]])

            if currentHigh > currentSar:
                currentState.is_up_trend = True
                currentSar = previousState.extreme_point
                currentState.acceleration_factor = api.MinAf
                currentState.extreme_point = currentHigh
            elif currentLow < previousState.extreme_point:
                currentState.extreme_point = currentLow
                currentState.acceleration_factor = self.increase_acceleration_factor(previousState.acceleration_factor)

        api.Result[index + api.Shift] = currentSar

    def setup_initial_value(self, index, initialSar, isUpTrend, initialExtremePoint):
        api.Result[index + api.Shift] = initialSar
        api.Result[index + api.Shift - 1] = initialSar

        currentState = self.states.get_value(index)
        currentState.is_up_trend = isUpTrend
        currentState.extreme_point = initialExtremePoint
        currentState.acceleration_factor = api.MinAf

        previousState = self.states.get_value(index - 1)
        previousState.extreme_point = initialExtremePoint
        previousState.acceleration_factor = api.MinAf
        previousState.is_up_trend = isUpTrend

    def calculate_current_sar(self, index):
        previousState = self.states.get_value(index - 1)
        previousSar = api.Result[index + api.Shift - 1]

        currentSar = previousSar + previousState.acceleration_factor * (previousState.extreme_point - previousSar)
        return currentSar

    def copy_state(self, from_state, to_state):
        to_state.extreme_point = from_state.extreme_point
        to_state.is_up_trend = from_state.is_up_trend
        to_state.acceleration_factor = from_state.acceleration_factor

    def get_min(self, values):
        notNaNValues = [v for v in values if math.isnan(v) == False]
        return min(notNaNValues) if len(notNaNValues) > 0 else float("nan")

    def get_max(self, values):
        notNaNValues = [v for v in values if math.isnan(v) == False]
        return max(notNaNValues) if len(notNaNValues) > 0 else float("nan")

    def increase_acceleration_factor(self, acceleration_factor):
        increased_acceleration_factor = acceleration_factor + api.MinAf
        if increased_acceleration_factor > api.MaxAf:
            return acceleration_factor

        return increased_acceleration_factor

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

class SarIndexState():
    def __init__(self):
        self.extreme_point = 0.0
        self.acceleration_factor = 0.0
        self.is_up_trend = False
