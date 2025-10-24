import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChandeMomentumOscillator():
    def initialize(self):
        if api.Source is None:
            api.Source = api.Bars.ClosePrices
        self.difference = api.CreateDataSeries()
        
    def calculate(self, index):
        outputIndex = index + api.Shift

        self.difference[index] = api.Source[index] - api.Source[index - 1] if index > 0 else float('nan')

        if index < api.Periods:
            api.Result[outputIndex] = float('nan')
            return

        sumPositive = 0
        sumNegative = 0
        
        for i in range(api.Periods):
            difference = self.difference[index - i]
            if difference > 0:
                sumPositive += difference;
            else:
                sumNegative += abs(difference)

        api.Result[outputIndex] = float('nan') if sumPositive + sumNegative == 0 else (sumPositive - sumNegative) / (sumPositive + sumNegative) * 100