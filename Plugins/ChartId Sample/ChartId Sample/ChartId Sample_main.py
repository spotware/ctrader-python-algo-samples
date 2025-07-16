import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartIdSample():
    def on_start(self):
        # Assigning custom handlers for the ChartManager.FramesAdded and ChartManager.FramesRemoved events
        api.ChartManager.FramesAdded += self.on_chartManager_frames_added;
        api.ChartManager.FramesRemoved += self.on_chartManager_frames_removed;
        
    def on_chartManager_frames_added(self, args):
        # Iterating over a collection of removed Frames
        for frame in args.AddedFrames:
            # Checking if a removed Frame is a ChartFrame
            if isinstance(frame.__implementation__, ChartFrame):
                # Downcasting the Frame to a ChartFrame and printing the message
                chartFrame = ChartFrame(frame)
                api.Print(f"Chart {chartFrame.Chart.Id} added");

    def on_chartManager_frames_removed(self, args):
        # Iterating over a collection of removed Frames
        for frame in args.RemovedFrames:
            # Checking if a removed Frame is a ChartFrame
            if isinstance(frame.__implementation__, ChartFrame):
                # Downcasting the Frame to a ChartFrame and printing the message
                chartFrame = ChartFrame(frame)
                api.Print(f"Chart {chartFrame.Chart.Id} removed");
