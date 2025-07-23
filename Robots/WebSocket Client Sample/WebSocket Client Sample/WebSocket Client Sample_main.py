import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import Uri

TARGET_URI = Uri("wss://marketdata.tradermade.com/feedadv")

class WebSocketClientSample():
    def on_start(self):
        self.webSocketClient = WebSocketClient()
        # Connecting to the API and sending the initial message
        self.webSocketClient.Connect(TARGET_URI)
        # Declaring a custom handler for the TextReceived event
        self.webSocketClient.TextReceived += self.on_text_received
        self.webSocketClient.Send("{\"userKey\":\"PasteStreamingKeyHere\", \"symbol\":\"EURUSD\"}")

    def on_text_received(self, args):
        if len(args.Text) > 0: 
            api.Print(args.Text)