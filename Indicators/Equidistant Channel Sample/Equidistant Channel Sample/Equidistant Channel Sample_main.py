import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class EquidistantChannelSample():
    def initialize(self):
        channel = api.Chart.DrawEquidistantChannel(
            "EquidistantChannel",
            api.Chart.FirstVisibleBarIndex,
            api.Bars.LowPrices[api.Chart.FirstVisibleBarIndex],
            api.Chart.LastVisibleBarIndex,
            api.Bars.HighPrices[api.Chart.LastVisibleBarIndex],
            20 * api.Symbol.PipSize,
            Color.Red)

        channel.IsInteractive = True