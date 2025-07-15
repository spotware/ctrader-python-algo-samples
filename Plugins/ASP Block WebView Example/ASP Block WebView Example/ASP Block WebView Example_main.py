import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ASPBlockWebViewExample():
    def on_start(self):
        block = api.Asp.SymbolTab.AddBlock("My title")
        block.Height = 500
        block.IsExpanded = True

        webView = WebView()
        block.Child = webView

        webView.NavigateAsync("https://ctrader.com/")
