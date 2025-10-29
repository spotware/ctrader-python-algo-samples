import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class VolumeROC():
    def calculate(self, index):
        if index < api.Periods:
            return

        volumePeriodsAgo = api.Bars.TickVolumes[index - api.Periods]
        volume = api.Bars.TickVolumes[index]
        
        api.Result[index + api.Shift] = (volume - volumePeriodsAgo) * 100 / volumePeriodsAgo