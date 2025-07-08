import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class AccessRightSample():
    def initialize(self):
        api.Print("Indicator with full access rights.")
        
    def calculate(self, index):
        pass