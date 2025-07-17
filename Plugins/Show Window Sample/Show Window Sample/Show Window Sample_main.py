import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ShowWindowSample():
    def on_start(self):
        addTakeProfitButton = Button()
        addTakeProfitButton.BackgroundColor = Color.SeaGreen
        addTakeProfitButton.Height = 50
        addTakeProfitButton.Text = "Add Take Profit"
        addTakeProfitButton.Click += self.on_add_take_profit_button_click

        window = Window()
        window.Height = 150
        window.Width = 150
        window.Padding = Thickness(5, 10, 10, 5)

        window.Child = addTakeProfitButton;
        window.Show();

    def on_add_take_profit_button_click(self, args):
        for position in api.Positions:
            if position.TakeProfit is None:
                position.ModifyTakeProfitPips(20)