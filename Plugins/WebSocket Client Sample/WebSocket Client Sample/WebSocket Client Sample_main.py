import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import TimeSpan, Uri

TARGET_URI = Uri("ws://localhost:1337")

class WebSocketClientSample():
    def on_start(self):
        webSocketClientOptions = WebSocketClientOptions()
        webSocketClientOptions.KeepAliveInterval = TimeSpan(0, 1, 30)
        webSocketClientOptions.UseDefaultCredentials = True

        self.webSocketClient = WebSocketClient(webSocketClientOptions)

        # Connecting to the API and sending the initial message
        self.webSocketClient.Connect(TARGET_URI)
        self.webSocketClient.Send("Hello")

        # Declaring a custom handler for the TextReceived event
        self.webSocketClient.TextReceived += self.on_text_received
            
        # Adding our TextBlock as a child of a custom AspBlock
        aspBlock = api.Asp.SymbolTab.AddBlock("WebSocket Client Sample");
        aspBlock.Height = 300;

        self.textBlock = TextBlock()
        self.textBlock.Text = "Listening..."
        self.textBlock.FontSize = 20
        self.textBlock.FontWeight = FontWeight.ExtraBold
        self.textBlock.TextAlignment = TextAlignment.Center
        self.textBlock.Padding = Thickness(5, 5, 5, 5)

        aspBlock.Child = self.textBlock;
        
    def on_text_received(self, args):
        # Updading the text inside the TextBlock on every piece of text received
        if len(args.Text) > 0: 
            self.textBlock.Text = f"Received: {args.Text}"

    def on_stop(self):
        # The WebSocketClient must be disposed of in OnStop,  otherwise it will consume system resources
        self.webSocketClient.Close(WebSocketClientCloseStatus.NormalClosure)
