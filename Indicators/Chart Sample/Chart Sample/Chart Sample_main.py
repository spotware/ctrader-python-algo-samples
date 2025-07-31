import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class ChartSample():
    def initialize(self):
        api.Chart.ChartTypeChanged += lambda _: self.add_chart_info_grid()
        api.Chart.ColorsChanged += lambda _: self.add_chart_info_grid()
        api.Chart.DisplaySettingsChanged += lambda _: self.add_chart_info_grid()
        api.Chart.Drag += lambda _: self.add_chart_info_grid()
        api.Chart.DragEnd += lambda _: self.add_chart_info_grid()
        api.Chart.DragStart += lambda _: self.add_chart_info_grid()
        api.Chart.IndicatorAreaAdded += lambda _: self.add_chart_info_grid()
        api.Chart.IndicatorAreaRemoved += lambda _: self.add_chart_info_grid()
        api.Chart.MouseMove += self.on_chart_mouse_move
        api.Chart.MouseLeave += self.on_chart_mouse_leave
        api.Chart.MouseWheel += self.on_chart_mouse_wheel
        api.Chart.ObjectsAdded += lambda _: self.update_chart_objects_count()
        api.Chart.ObjectsRemoved += lambda _: self.update_chart_objects_count()

        api.Chart.ZoomChanged += lambda _: self.add_chart_info_grid()

        self.add_chart_info_grid()

    def on_chart_mouse_move(self, args):
        if self.mouseLocationTextBlock is None:
            return
        
        self.mouseLocationTextBlock.Text = f"({args.MouseX}, {args.MouseY})"

    def on_chart_mouse_leave(self, args):
        if self.mouseLocationTextBlock is None:
            return
        
        self.mouseLocationTextBlock.Text = "(Null, Null)"
        self.mouseWheelDeltaTextBlock.Text = "0"

    def on_chart_mouse_wheel(self, args):
        if self.mouseWheelDeltaTextBlock is None:
            return
        
        self.mouseWheelDeltaTextBlock.Text = str(args.Delta)

    def update_chart_objects_count(self):
        self.objectsNumberTextBlock.Text = str(api.Chart.Objects.Count)

    def get_text_block(self, text):
        textBlock = TextBlock()
        textBlock.Text = text
        textBlock.Style = self.style
        return textBlock

    def add_chart_info_grid(self):
        if hasattr(self, 'grid') and self.grid is not None:
            api.Chart.RemoveControl(self.grid)

        self.grid = Grid(10, 2)
        self.grid.BackgroundColor = Color.Gold
        self.grid.Opacity = 0.6
        self.grid.HorizontalAlignment = HorizontalAlignment.Left
        self.grid.VerticalAlignment = VerticalAlignment.Bottom

        self.style = Style()

        self.style.Set(ControlProperty.Margin, Thickness(5))
        self.style.Set(ControlProperty.FontWeight, FontWeight.ExtraBold)
        self.style.Set(ControlProperty.ForegroundColor, Color.Red)

        self.grid.AddChild(self.get_text_block("Height"), 0, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.Height)), 0, 1)
        self.grid.AddChild(self.get_text_block("Width"), 1, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.Width)), 1, 1)
        self.grid.AddChild(self.get_text_block("Zoom Level"), 2, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.ZoomLevel)), 2, 1)
        self.grid.AddChild(self.get_text_block("Objects #"), 3, 0)

        self.objectsNumberTextBlock = self.get_text_block(str(api.Chart.Objects.Count))

        self.grid.AddChild(self.objectsNumberTextBlock, 3, 1)

        self.grid.AddChild(self.get_text_block("Top Y"), 4, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.TopY)), 4, 1)
        self.grid.AddChild(self.get_text_block("Bottom Y"), 5, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.BottomY)), 5, 1)
        self.grid.AddChild(self.get_text_block("Type"), 6, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.ChartType)), 6, 1)
        self.grid.AddChild(self.get_text_block("Mouse Location"), 7, 0)

        self.mouseLocationTextBlock = self.get_text_block("(Null, Null)")

        self.grid.AddChild(self.mouseLocationTextBlock, 7, 1)
        self.grid.AddChild(self.get_text_block("Indicator Areas #"), 8, 0)
        self.grid.AddChild(self.get_text_block(str(api.Chart.IndicatorAreas.Count)), 8, 1)
        self.grid.AddChild(self.get_text_block("Mouse Wheel Delta"), 9, 0)

        self.mouseWheelDeltaTextBlock = self.get_text_block("0")

        self.grid.AddChild(self.mouseWheelDeltaTextBlock, 9, 1)

        api.Chart.AddControl(self.grid)