import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class WebViewCustomFrameSample():
    def on_start(self):
        self.ctrader_forum_webview = WebView()
        self.ctrader_forum_webview.Loaded += self.on_ctrader_forum_webview_loaded

        ctrader_forum_frame = api.ChartManager.AddCustomFrame("cTrader Forum")
        ctrader_forum_frame.Child = self.ctrader_forum_webview

        self.spotware_webview = WebView()
        self.spotware_webview.Loaded += self.on_spotware_webview_loaded

        spotware_frame = api.ChartManager.AddCustomFrame("Spotware Site")
        spotware_frame.Child = self.spotware_webview

        api.ChartManager.ChartContainers.MainChartContainer.Mode = ChartMode.Multi

    def on_ctrader_forum_webview_loaded(self, args):
        args.WebView.NavigateAsync("https://community.ctrader.com/")

    def on_spotware_webview_loaded(self, args):
        args.WebView.NavigateAsync("https://www.spotware.com/")
