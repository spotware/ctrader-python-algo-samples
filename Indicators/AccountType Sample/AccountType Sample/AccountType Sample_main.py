import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AccountTypeSample():
    def initialize(self):
        text = f"Account Type: {api.Account.AccountType}"
        api.Chart.DrawStaticText("text", text, VerticalAlignment.Top, HorizontalAlignment.Right, Color.Red)
        
    def calculate(self, index):
        pass