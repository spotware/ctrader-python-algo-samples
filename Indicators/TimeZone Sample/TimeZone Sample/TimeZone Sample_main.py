import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import TimeZoneInfo

class TimeZoneSample():
    def initialize(self):
        # You can get user platform time zone offset like this
        platformUserSelectedTimeZoneOffset = api.Application.UserTimeOffset

        estTime = self.get_eastern_standard_time()
        api.Print(estTime.ToString("o"))

    def get_eastern_standard_time(self):
        easternTimeZone = TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time")
        return TimeZoneInfo.ConvertTimeFromUtc(api.Server.TimeInUtc, easternTimeZone)