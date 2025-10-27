import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class MoneyFlowIndex():
    def calculate(self, index):
        if index < api.Periods:
            return

        positiveMoneyFlow = self.calculate_money_flow(index, lambda current, previous : current > previous)
        negativeMoneyFlow = self.calculate_money_flow(index, lambda current, previous : current < previous)

        moneyFlowRatio = 0 if negativeMoneyFlow == 0 else positiveMoneyFlow / negativeMoneyFlow

        api.Result[index + api.Shift] = 100 - 100 / (1 + moneyFlowRatio)

    def calculate_money_flow(self, index, addCondition):
        moneyFlow = 0.0

        for i in range(api.Periods):
            currentIndex = index - i
            currentTypicalPrice = api.Bars.TypicalPrices[currentIndex]
            prevTypicalPrice = api.Bars.TypicalPrices[currentIndex - 1]

            if addCondition(currentTypicalPrice, prevTypicalPrice):
                moneyFlow += currentTypicalPrice * api.Bars.TickVolumes[currentIndex]

        return moneyFlow