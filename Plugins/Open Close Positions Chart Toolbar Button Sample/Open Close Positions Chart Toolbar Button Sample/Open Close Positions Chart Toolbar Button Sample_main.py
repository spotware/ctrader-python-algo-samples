import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
from System import Func, Action


class OpenClosePositionsChartToolbarButtonSample():
    def on_start(self):
        openPositionsCommand = api.Commands.Add(CommandType.ChartContainerToolbar, Action[CommandArgs](self.open_positions_command_callback), SvgIcon(icon));
        openPositionsCommand.ToolTip = "Open Positions";

        closePositionsCommand = api.Commands.Add(CommandType.ChartContainerToolbar, Func[CommandArgs, CommandResult](self.close_all_positions_command_callback), SvgIcon(icon));
        closePositionsCommand.ToolTip = "Close All Positions"
        
    def open_positions_command_callback(self, args):
        api.ExecuteMarketOrder(TradeType.Buy, "EURUSD", api.Symbols.GetSymbol("EURUSD").VolumeInUnitsMin); 
        api.ExecuteMarketOrder(TradeType.Buy, "USDJPY", api.Symbols.GetSymbol("USDJPY").VolumeInUnitsMin); 
        api.ExecuteMarketOrder(TradeType.Sell, "EURGBP", api.Symbols.GetSymbol("EURGBP").VolumeInUnitsMin);  
    
    def close_all_positions_command_callback(self, args):
        buttonStyle = Style()

        buttonStyle.Set(ControlProperty.Margin, Thickness(0, 5, 0, 0))
        buttonStyle.Set(ControlProperty.Width, 150)

        closePositionsButton = Button()
        closePositionsButton.Text = "Close All Positions"
        closePositionsButton.Style = buttonStyle  
        closePositionsButton.Click += self.on_close_positions_button_click

        stackPanel = StackPanel()
        stackPanel.AddChild(closePositionsButton)

        return CommandResult(stackPanel)

    def on_close_positions_button_click(self, args):
        for position in api.Positions:
            position.Close()

icon = "<svg class='w-6 h-6 text-gray-800 dark:text-white' aria-hidden='true' xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24'><path stroke='#BFBFBF' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M11 6.5h2M11 18h2m-7-5v-2m12 2v-2M5 8h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm0 12h2a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm12 0h2a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Zm0-12h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1Z'/></svg>"