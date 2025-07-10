import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AlgoRegistrySample():
    def initialize(self):
        if not (api.AlgoRegistry.Exists("Rapid SMA") and api.AlgoRegistry.Exists("Swirling SMA")):
            MessageBox.Show("Required indicators are not installed!", "Warning!", MessageBoxButton.OK, MessageBoxImage.Warning, MessageBoxResult.OK)
        else:
            api.ChartIndicators.Add("Rapid SMA")
            api.ChartIndicators.Add("Swirling SMA")