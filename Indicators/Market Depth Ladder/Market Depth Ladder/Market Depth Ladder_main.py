import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import DayOfWeek

class MarketDepthLadder():
    def initialize(self):
        self.chartObjectNamesSuffix = "Ladder"
        self.marketDepth = api.MarketData.GetMarketDepth(api.Symbol.Name)

    def calculate(self, index):
        if api.IsLastBar == False:
            return

        self.remove_ladder()
        self.plot_ladder(index)

    def remove_ladder(self):
        ladderChartObjectNames = [chartObject.Name for chartObject in api.Chart.Objects if chartObject.Name.endswith(self.chartObjectNamesSuffix)]
        
        for chartObjectName in ladderChartObjectNames:
            api.Chart.RemoveObject(chartObjectName)

    def plot_ladder(self, index):
        startBarIndex = index + api.Offset;

        startTime = api.Bars.OpenTimes[startBarIndex] if index - startBarIndex > 0 else self.get_open_time(startBarIndex)

        if self.marketDepth.AskEntries.Count == 0 or self.marketDepth.BidEntries.Count == 0:
            return

        minBidVolume = min([entry.VolumeInUnits for entry in self.marketDepth.BidEntries])
        maxBidVolume = max([entry.VolumeInUnits for entry in self.marketDepth.BidEntries])

        minAskVolume = min([entry.VolumeInUnits for entry in self.marketDepth.AskEntries])
        maxAskVolume = max([entry.VolumeInUnits for entry in self.marketDepth.AskEntries])

        minVolume = min(minBidVolume, minAskVolume)
        maxVolume = max(maxBidVolume, maxAskVolume)

        minAllowed = 0

        for depthEntry in self.marketDepth.BidEntries:
            objName = f"{depthEntry.Price}_Bid_{self.chartObjectNamesSuffix}"
            volumeAmount = self.get_min_max(depthEntry.VolumeInUnits, minVolume, maxVolume, minAllowed, api.MaxLength)
            endIndex = int(startBarIndex - volumeAmount)
            endTime = self.get_open_time(endIndex)
            rectangle = api.Chart.DrawRectangle(objName, startTime, depthEntry.Price, endTime, depthEntry.Price, api.BuyOrdersColor, 1, LineStyle.Solid)
            rectangle.IsFilled = True

        for depthEntry in self.marketDepth.AskEntries:
            objName = f"{depthEntry.Price}_Ask_{self.chartObjectNamesSuffix}"
            volumeAmount = self.get_min_max(depthEntry.VolumeInUnits, minVolume, maxVolume, minAllowed, api.MaxLength)
            endIndex = int(startBarIndex - volumeAmount)
            endTime = self.get_open_time(endIndex)
            rectangle = api.Chart.DrawRectangle(objName, startTime, depthEntry.Price, endTime, depthEntry.Price, api.SellOrdersColor, 1, LineStyle.Solid)
            rectangle.IsFilled = True
    
    def get_min_max(self, value, minValue, maxValue, minAllowedValue, maxAllowedValue):
        b = maxValue - minValue if maxValue - minValue != 0 else 1 / maxValue
        uninterpolate = (value - minValue) / b
        result = minAllowedValue * (1 - uninterpolate) + maxAllowedValue * uninterpolate
        return result

    def get_open_time(self, index):
        currentIndex = api.Bars.Count - 1
        timeDiff = self.get_time_diff()

        indexDiff = index - currentIndex
        indexDiffAbs = abs(indexDiff)

        result = api.Bars.OpenTimes[int(index)] if indexDiff <= 0 else api.Bars.OpenTimes[currentIndex]
        if indexDiff > 0:
            for i in range(1, indexDiffAbs + 1):
                result = result.Add(timeDiff)
                while (result.DayOfWeek == DayOfWeek.Saturday or result.DayOfWeek == DayOfWeek.Sunday):
                    result = result.Add(timeDiff)

        barIndexFraction = index % 1
        barIndexFractionInMinutes = timeDiff.TotalMinutes * barIndexFraction

        result = result.AddMinutes(barIndexFractionInMinutes)
        return result

    def get_time_diff(self):
        index = api.Bars.Count - 1

        if index < 4:
            raise Exception("Not enough data in market series to calculate the time difference")

        timeDiffs = {}

        for i in range(index, index - 4, -1):
            diff = api.Bars.OpenTimes[i] - api.Bars.OpenTimes[i - 1]
            if diff in timeDiffs:
                timeDiffs.update({diff: timeDiffs[diff] + 1})
            else:
                timeDiffs[diff] = 1
        return max(timeDiffs, key=timeDiffs.get)