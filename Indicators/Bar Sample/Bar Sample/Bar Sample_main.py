import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class BarSample():        
    def calculate(self, index):
        currentBar = api.Bars[index]
        api.Print(f"Open: {currentBar.Open} | High: {currentBar.High} | Low: {currentBar.Low} | Close: {currentBar.Close} | Open Time: {currentBar.OpenTime} | Volume: {currentBar.TickVolume}")