import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

class CustomFrameSample():
    def on_start(self):
        aspBlock = api.Asp.SymbolTab.AddBlock("Custom Frame Sample");

        panel = StackPanel()
        
        addCustomFrameButton = Button()
        addCustomFrameButton.Text = "Add Custom Frame"
        addCustomFrameButton.Margin = Thickness(5)    
        addCustomFrameButton.Click += self.on_add_custom_frame_button_click
            
        panel.AddChild(addCustomFrameButton)

        removeCustomFrameButton = Button()
        removeCustomFrameButton.Text = "Remove Custom Frame"
        removeCustomFrameButton.Margin = Thickness(5) 
        removeCustomFrameButton.Click += self.on_remove_custom_frame_button_click
            
        panel.AddChild(removeCustomFrameButton)

        detachCustomFrameButton = Button()
        detachCustomFrameButton.Text = "Detach Custom Frame"
        detachCustomFrameButton.Margin = Thickness(5) 
        detachCustomFrameButton.Click += self.on_detach_custom_frame_button_click
            
        panel.AddChild(detachCustomFrameButton);
         
        attachCustomFrameButton = Button()
        attachCustomFrameButton.Text = "Attach Custom Frame"
        attachCustomFrameButton.Margin = Thickness(5) 
        attachCustomFrameButton.Click += self.on_attach_custom_frame_button_click
            
        panel.AddChild(attachCustomFrameButton)
            
        aspBlock.Child = panel

    def on_add_custom_frame_button_click(self, args):
        customFrame = api.ChartManager.AddCustomFrame("Custom Frame");

        textBlock = TextBlock()
        textBlock.Text = f"Custom Frame {customFrame.Id} Child Control"
        textBlock.FontSize = 32
        textBlock.HorizontalAlignment = HorizontalAlignment.Center
        textBlock.VerticalAlignment = VerticalAlignment.Center

        customFrame.Child = textBlock

    def on_remove_custom_frame_button_click(self, args):
        for frame in api.ChartManager:
            if isinstance(frame.__implementation__, CustomFrame) == False:
                continue
            customFrame = CustomFrame(frame)
            api.ChartManager.RemoveFrame(customFrame.Id)
            break

    def on_detach_custom_frame_button_click(self, args):
        for frame in api.ChartManager:
            if isinstance(frame.__implementation__, CustomFrame) == False:
                continue
            customFrame = CustomFrame(frame)
            if customFrame.IsAttached == False:
                continue
            customFrame.Detach()
            break
         
    def on_attach_custom_frame_button_click(self, args):
        for frame in api.ChartManager:
            if isinstance(frame.__implementation__, CustomFrame) == False:
                continue
            customFrame = CustomFrame(frame)
            if customFrame.IsAttached == True:
                continue
            customFrame.Attach()
            break