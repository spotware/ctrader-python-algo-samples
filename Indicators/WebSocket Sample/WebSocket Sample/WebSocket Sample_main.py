import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import TimeSpan, Uri

TARGET_URI = Uri("ws://bestindicator.io:8000")

class WebSocketSample():
    def initialize(self):
        webSocketClientOptions = WebSocketClientOptions()
        webSocketClientOptions.KeepAliveInterval = TimeSpan(0, 1, 30)
        webSocketClientOptions.UseDefaultCredentials = True
        self.webSocketClient = WebSocketClient(webSocketClientOptions)
        # Declaring a custom handler for the TextReceived event
        self.webSocketClient.TextReceived += self.on_text_received
        # Connecting to the API and sending the initial message
        self.webSocketClient.Connect(TARGET_URI)
        self.currentResultFromService = 0
        self.simpleMovingAverage = api.Indicators.SimpleMovingAverage(api.Bars.ClosePrices, 14)

    def on_text_received(self, args):
        if args.Text is None or len(args.Text) == 0: 
            return
        # Simulating usage of received data from an external service
        # On every text received, parse it into a float
        # and store it for usage
        self.currentResultFromService = float(args.Text)

    def calculate(self, index):
        # Modifying the result of the SimplveMovingAverage
        # by multiplying it with the results attained from the
        # external service
        api.Result[index] = self.simpleMovingAverage.Result[index] * self.currentResultFromService