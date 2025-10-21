import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *
from enum import Enum

class SampleLinesTrader():
    how_to_use_text = "How to use:\nCtrl + Left Mouse Button - Draw Breakout line\nShift + Left Mouse Button - Draw Retracement line"
    how_to_use_object_name = "LinesTraderText"

    def on_start(self):
        self.draw_manager = SignalLineDrawManager()
        self.signal_line_repository = SignalLineRepository(api.Chart)

        if api.ShowHowToUse:
            self.show_how_to_use_text()
            api.Chart.MouseDown += self.on_chart_mouse_down

    def on_tick(self):
        lastBarIndex = api.Bars.Count - 1;

        for signalLine in self.signal_line_repository.get_lines():
            if signalLine.can_execute(api.Bid, lastBarIndex):
                signalLine.mark_as_executed()
                message = f"{api.Time} Signal line {signalLine.tradeType}{signalLine.signalType} was executed on {api.SymbolName}"
                api.Print(message)

                if api.IsTradingAllowed:
                    api.ExecuteMarketOrder(signalLine.tradeType, api.SymbolName, api.Volume, "LinesTrader cBot", api.StopLossPips, api.TakeProfitPips)

                if api.IsEmailAllowed:
                    api.Notifications.SendEmail(api.EmailAddress, api.EmailAddress, "LinesTrader Alert", message)

    def on_chart_mouse_down(self, args):
        api.Chart.MouseDown -= self.on_chart_mouse_down
        self.hide_how_to_use_text()

    def show_how_to_use_text(self):
        api.Chart.DrawStaticText(self.how_to_use_object_name, self.how_to_use_text, VerticalAlignment.Center, HorizontalAlignment.Center, api.Chart.ColorSettings.ForegroundColor)

    def hide_how_to_use_text(self):
        api.Chart.RemoveObject(self.how_to_use_object_name)

class SignalLineDrawManager():
    def __init__(self):
        self.chart = api.Chart
        self.currentProtoSignalLine = None
        self.status_text_name = "ProtoSignalLineStatus"
        self.chart.DragStart += self.on_chart_drag_start
        self.chart.DragEnd += self.on_chart_drag_end
        self.chart.Drag += self.on_chart_drag

    def on_chart_drag_start(self, args):
        if args.ChartArea != args.Chart:
            return

        signalType = self.get_signal_type(args)

        if signalType is not None:
            self.chart.IsScrollingEnabled = False
            self.currentProtoSignalLine = ProtoSignalLine(signalType, args.TimeValue, args.YValue)
            self.update_status()
        else:
            self.currentProtoSignalLine = None

    def on_chart_drag_end(self, args):
        if self.currentProtoSignalLine is None:
            return

        self.currentProtoSignalLine.complete(args.TimeValue, args.YValue)
        self.currentProtoSignalLine = None

        self.chart.IsScrollingEnabled = True
        self.chart.RemoveObject(self.status_text_name)

    def on_chart_drag(self, args):
        if self.currentProtoSignalLine is None:
            return

        self.currentProtoSignalLine.update(args.TimeValue, args.YValue)
        self.update_status()

    def update_status(self):
        text = f"Creating {self.currentProtoSignalLine.line_label()} line"
        self.chart.DrawStaticText(self.status_text_name, text, VerticalAlignment.Top, HorizontalAlignment.Left, self.chart.ColorSettings.ForegroundColor)

    def get_signal_type(self, args):
        if args.CtrlKey and args.ShiftKey == False:
            return SignalType.Breakout
        if args.CtrlKey == False and args.ShiftKey:
            return SignalType.Retracement

        return None;

class SignalLineRepository():
    def __init__(self, chart):
        self.chart = chart
        self.signalLines = {}

        for chartTrendLine in self.chart.FindAllObjects[ChartTrendLine]():
            self.try_add_signal_line(chartTrendLine)

        self.chart.ObjectsAdded += self.on_chart_object_added
        self.chart.ObjectsRemoved += self.on_chart_object_removed
        self.chart.ObjectsUpdated += self.on_chart_object_updated

    def get_lines(self):
        return list(self.signalLines.values())

    def try_add_signal_line(self, chartObject):
        if isinstance(chartObject.__implementation__, ChartTrendLine) == False:
            return

        chartTrendLine = ChartTrendLine(chartObject);

        if chartTrendLine is not None and self.is_signal_line(chartTrendLine):
            self.signalLines[chartTrendLine.Name] = self.create_signal_line(chartTrendLine)

    def try_remove_signal_line(self, chartObject):
        if chartObject.Name in self.signalLines:
            del self.signalLines[chartObject.Name]

    def on_chart_object_added(self, args):
        if args.Area != args.Chart:
            return

        for chartObject in args.ChartObjects:
            self.try_add_signal_line(chartObject)

    def on_chart_object_updated(self, args):
        if args.Area != args.Chart:
            return

        for chartObject in args.ChartObjects:
            self.try_remove_signal_line(chartObject)
            self.try_add_signal_line(chartObject)

    def on_chart_object_removed(self, args):
        if args.Area != args.Chart:
            return

        for chartObject in args.ChartObjects:
            self.try_remove_signal_line(chartObject)

    def create_signal_line(self, chartTrendLine):
        signalType = self.get_line_signal_type(chartTrendLine)
        tradeType = self.get_line_trade_type(chartTrendLine)
        signalLine = SignalLine(chartTrendLine, signalType, tradeType)
        return signalLine

    def is_signal_line(self, line):
        return line.Comment in SignalLineLabels.get_all_labels()

    def get_line_signal_type(self, line):
        comment = line.Comment;
        if comment == SignalLineLabels.BuyBreakoutLabel or comment == SignalLineLabels.SellBreakoutLabel:
                return SignalType.Breakout
        if comment == SignalLineLabels.BuyRetraceLabel or comment == SignalLineLabels.SellRetraceLabel:
                return SignalType.Retracement
        
        raise Exception("Invalid comment")

    def get_line_trade_type(self, line):
        comment = line.Comment;

        if comment == SignalLineLabels.BuyBreakoutLabel or comment == SignalLineLabels.BuyRetraceLabel:
            return TradeType.Buy

        if comment == SignalLineLabels.SellBreakoutLabel or comment == SignalLineLabels.SellRetraceLabel:
            return TradeType.Sell;

        raise Exception("Invalid comment")

class ProtoSignalLine():
    BuyLineColor = Color.Green
    SellLineColor = Color.Red

    def __init__(self, signalType, startTimeValue, startYValue):
        self.chart = api.Chart
        self.signalType = signalType
        self.symbol = api.Symbol

        self.line = None
        self.line = self.chart.DrawTrendLine(f"LinesTrader {self.chart.Objects.Count}", startTimeValue, startYValue, startTimeValue, startYValue, self.line_color())

        self.line.ExtendToInfinity = True
        self.line.Thickness = 2
        self.line.IsInteractive = True

    def is_price_above_Line(self):
        return self.line is not None and self.symbol.Bid >= self.line.CalculateY(self.chart.Bars.Count - 1)

    def line_trade_type(self):
        if self.signalType == SignalType.Breakout:
            return TradeType.Sell if self.is_price_above_Line() else TradeType.Buy
        else:
            return TradeType.Buy if self.is_price_above_Line() else TradeType.Sell

    def line_color(self):
        return self.BuyLineColor if self.line_trade_type() == TradeType.Buy else self.SellLineColor

    def line_label(self):
        if self.signalType == SignalType.Breakout:
            return SignalLineLabels.BuyBreakoutLabel if self.line_trade_type() == TradeType.Buy else SignalLineLabels.SellBreakoutLabel
        else:
            return SignalLineLabels.BuyRetraceLabel if self.line_trade_type() == TradeType.Buy else SignalLineLabels.SellRetraceLabel

    def can_complete(self):
        return self.line.Time1 != self.line.Time2 or abs(self.line.Y1 - self.line.Y2) >= self.symbol.PipValue

    def update(self, timeValue, yValue):
        self.line.Time2 = timeValue
        self.line.Y2 = yValue
        self.line.Color = self.line_color()

    def complete(self, timeValue, yValue):
        self.update(timeValue, yValue)

        if self.can_complete():
            self.line.Comment = self.line_label()
            self.line.IsInteractive = True
        else:
            self.chart.RemoveObject(self.line.Name)


class SignalLine():
    def __init__(self, chartTrendLine, signalType, tradeType):
        self.chartTrendLine = chartTrendLine
        self.signalType = signalType
        self.tradeType = tradeType

    def mark_as_executed(self):
        self.chartTrendLine.Thickness = 1
        self.chartTrendLine.Color = Color.FromArgb(150, self.chartTrendLine.Color)

    def can_execute(self, price, barIndex):
        if self.chartTrendLine.Thickness <= 1:
            return False

        lineValue = self.chartTrendLine.CalculateY(barIndex)

        match self.signalType:
            case SignalType.Breakout:
                return self.can_execute_for_breakout(price, lineValue)
            case SignalType.Retracement:
                return self.can_execute_for_retrace(price, lineValue)
            case _:
                raise Exception("Unknown signal type");

    def can_execute_for_breakout(self, price, lineValue):
        return self.tradeType == TradeType.Buy and price > lineValue or self.tradeType == TradeType.Sell and price < lineValue

    def can_execute_for_retrace(self, price, lineValue):
        return self.tradeType == TradeType.Buy and price <= lineValue or self.tradeType == TradeType.Sell and price >= lineValue

class SignalType(Enum):
    Breakout = 1
    Retracement = 2

class SignalLineLabels():
    BuyBreakoutLabel = "BuyBreakout"
    SellBreakoutLabel = "SellBreakout"
    BuyRetraceLabel = "BuyRetracement"
    SellRetraceLabel = "SellRetracement"

    def get_all_labels():
        return [
            SignalLineLabels.BuyBreakoutLabel,
            SignalLineLabels.SellBreakoutLabel,
            SignalLineLabels.BuyRetraceLabel,
            SignalLineLabels.SellRetraceLabel
        ]
