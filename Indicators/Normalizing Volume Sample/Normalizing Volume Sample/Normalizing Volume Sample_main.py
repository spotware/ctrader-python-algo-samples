import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from cAlgo.Indicators import *

class NormalizingVolumeSample():
    def initialize(self):
        volumeInUnits = api.VolumeAmount if api.VolumeUnit == VolumeUnit.Units else api.Symbol.QuantityToVolumeInUnits(api.VolumeAmount)
        normalizedVolume = api.Symbol.NormalizeVolumeInUnits(volumeInUnits, api.RoundingMode)
        api.Print(normalizedVolume)