import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class UserTimeOffsetChangedEventArgsSample():
    def initialize(self):
        api.Application.UserTimeOffsetChanged += self.on_application_user_time_offset_changed

    def on_application_user_time_offset_changed(self, args):
        api.Print(f"User time offset changed to: {args.UserTimeOffset}")