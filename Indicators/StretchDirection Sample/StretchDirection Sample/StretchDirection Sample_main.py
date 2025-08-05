import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *

import os.path
"""
We have to use .NET array and Byte
because image control source works only with
Svg string, .NET byte enumerable, and .NET Bitmap
"""
from System import Array, Byte

# Your algo must have FullAccess rights to use file API
class StretchDirectionSample():
    def initialize(self):
        if os.path.exists(api.ImageFilePath) == False:
            api.Print(f"Image not found: {api.ImageFilePath}")
            return

        imageFile = open(api.ImageFilePath, 'rb')
        imageBytes = imageFile.read()

        # Storing image file bytes inside .NET array
        imageBytesArray = Array[Byte](len(imageBytes))

        for i, b in enumerate(imageBytes):
            imageBytesArray[i] = Byte(b)

        image = Image()
        # You can also set source to SVG string
        image.Source = imageBytesArray
        image.Width = 200
        image.Height = 200
        image.HorizontalAlignment = HorizontalAlignment.Center
        image.VerticalAlignment = VerticalAlignment.Center
        image.StretchDirection = api.StretchDirection

        api.Chart.AddControl(image);