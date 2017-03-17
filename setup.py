import sys
from cx_Freeze import setup, Executable


# GUI applications require a different base on Windows (the default is for a
# console application).

application_title = "PyPingCheck"
main_python_file = "main.py"

includefiles = ["ping.png"]


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
"packages": ["os","sys","subprocess","time","socket"],
"include_msvcr" : True
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    includefiles += [(r"C:\Program Files\Python36\Lib\site-packages\PyQt5\plugins","plugins")]
    includefiles += [(r"C:\Program Files\Python36\Lib\site-packages\PyQt5\translations","translations")]

cible = Executable(
script = "main.py",
icon = "ping.ico",
base=base
)

setup(  name = "PyPingCheck",
        version = "2.1",
        description = "GUI version !",
        options = {"build_exe": build_exe_options},
        executables = [cible])
