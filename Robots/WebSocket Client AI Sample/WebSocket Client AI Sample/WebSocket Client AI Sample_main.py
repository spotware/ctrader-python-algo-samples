import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from System import TimeSpan, Uri

TARGET_URI = Uri("ws://chatddt.com:8000")

class WebSocketClientAISample():
    def on_start(self):
        webSocketClientOptions = WebSocketClientOptions()
        webSocketClientOptions.KeepAliveInterval = TimeSpan(0, 1, 30)
        webSocketClientOptions.UseDefaultCredentials = True
        self.webSocketClient = WebSocketClient(webSocketClientOptions)
        # Declaring a custom handler for the TextReceived event
        self.webSocketClient.TextReceived += self.on_text_received
        # Connecting to the API and sending the initial message
        self.webSocketClient.Connect(TARGET_URI)
        self.webSocketClient.Send("You are an expert forex trader and market analyst")

    def on_text_received(self, args):
        if len(args.Text) > 0: 
            MessageBox.Show(args.Text)

    def on_bar_closed(self):
        # Attaining data for the current bar that has just closed and the preceding bar
        currentBar = api.Bars.LastBar
        previousBar = api.Bars.Last(Bars.Count - 2)
            
        # Creating a prompt for market analysis based on bar data
        marketPrompt = f"""\
            For the current bar, the high, low, open, and close were the following:
            {currentBar.High}, {currentBar.Low}, {currentBar.Open}, {currentBar.Close}. For the previous bar,
            these values were {previousBar.High}, {previousBar.Low}, {previousBar.Open}, {previousBar.Close}.
            Make predictions about the future.
            """
            
        # Sending the new prompt to the AI service
        self.webSocketClient.Send(marketPrompt);