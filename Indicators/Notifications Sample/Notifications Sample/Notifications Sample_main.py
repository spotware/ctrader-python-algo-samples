import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class NotificationsSample():
    def initialize(self):
        self.lastNotifiedBarIndex = 0

    def calculate(self, index):
        if api.IsLastBar == False or self.lastNotifiedBarIndex == index:
            return

        self.lastNotifiedBarIndex = index

        if api.Bars.Last(1).Close > api.Bars.Last(1).Open:
            self.notify("Up Bar Closed")
        elif api.Bars.Last(1).Close < api.Bars.Last(1).Open:
            self.notify("Down Bar Closed")

    def notify(self, message):
        if api.SoundFilePath is not None and len(api.SoundFilePath) > 0:
            api.Notifications.PlaySound(api.SoundFilePath)

        if api.SenderEmail is not None and len(api.SenderEmail) > 0 and api.ReceiverEmail is not None and len(api.ReceiverEmail) > 0:
            api.Notifications.SendEmail(api.SenderEmail, api.ReceiverEmail, "Notification", message)

        if api.ShowPopup:
            api.Notifications.ShowPopup("Notification", message, PopupNotificationState.Success)

        