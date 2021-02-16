import os
from pathlib import Path
class Controller:

    # path for the adb which come with NOX emulator.
    path = str(Path().absolute()) + "/adb"

    # Change the directory to it.
    os.chdir(path)
           

    def click(self, x, y):
        os.popen("adb shell input tap " + x+ " " + y)

