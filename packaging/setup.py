
import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "sys", "PIL"],
    "excludes": [],
    "include_files": [os.path.join("..", "devtools", "itemmake", "template.txt")]
}

# Base options
base = None
if sys.platform == "win32":
    base = "Console" # Use "Win32GUI" for GUI applications

# Target executable
target = Executable(
    script=os.path.join("..", "devtools", "itemmake", "itemmake.py"),
    base=base,
    target_name="ItemMake.exe",
    icon=None # Add icon path if available
)

setup(
    name="TamagotchiItemMake",
    version="1.0.0",
    description="Tamagotchi User Item Maker",
    options={"build_exe": build_exe_options},
    executables=[target]
)
