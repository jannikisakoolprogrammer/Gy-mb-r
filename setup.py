import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ['database/', 'language_files/']}

# base="Win32GUI" should be used only for Windows GUI app - test
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Gyoember",
    version = "0.1",
    description = "Learn Hungarian the hard way!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Gyoember.py", base=base)]
)