import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

import json

HTML = """
<body bgcolor='white'>
<div>
  <div>
    <span>ctid:</span>
    <span id='ctid'/>
  </div>
  <div>
    <span>account number:</span>
    <span id='account'/>
  </div>
  <div>
    <span>broker:</span>
    <span id='broker'/>
  </div>  
  <button onclick='closeAll()'>Close all positions</button>
<div>
</body>
<script>
function closeAll(){
  window.postMessage('close all message');
}
function updateValues(data){
  document.getElementById('ctid').innerHTML = data.ctid;
  document.getElementById('account').innerHTML = data.account;
  document.getElementById('broker').innerHTML = data.broker;
}
</script>
"""

class InteractiveWebView():
    def on_start(self):
        self.webView = WebView()
        self.webView.WebMessageReceived += self.on_webView_web_message_received

        block = api.Asp.SymbolTab.AddBlock("Interactive WebView")
        block.Child = self.webView
        block.Height = 300
        block.IsExpanded = True
        block.IsDetachable = False

        self.webView.NavigationCompleted += self.on_webView_navigation_completed
        self.webView.NavigateToStringAsync(HTML)

        api.Account.Switched += self.on_account_switched

    def on_webView_navigation_completed(self, args):
        self.update_account_info()

    def on_account_switched(self, args):
        self.update_account_info()

    def on_webView_web_message_received(self, args):
        if args.Message == "\"close all message\"":
            for position in api.Positions:
                position.Close();

    def update_account_info(self):
      data = {"ctid": api.Account.UserId, "account": api.Account.Number, "broker": api.Account.BrokerName}
      self.webView.ExecuteScript(f"updateValues({json.dumps(data)})");

