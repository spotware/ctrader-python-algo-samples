import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

# ATTENTION: To enable file system access, you need to modify the Robot attribute in Engine.cs:
# [Robot(AccessRights = AccessRights.FullAccess)]

# Path to the file that will be used for read/write operations
FILE_PATH = r"file.txt"

class FileSystemSample():
    def on_start(self):
        print("Robot started")
        
        # Create a new file and write initial content
        with open(FILE_PATH, "w") as file:
            file.write("Hello world!")

        # Append additional content to the existing file
        with open(FILE_PATH, "a") as file:
            file.write("\nSecond line")

        # Read and print all lines from the file
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.rstrip())  # Remove trailing newlines when printing
    
    # To learn more about cTrader Algo visit our Help Center:
    # https://help.ctrader.com/ctrader-algo/
