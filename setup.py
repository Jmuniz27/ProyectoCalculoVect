import sys
from cx_Freeze import setup, Executable

base = None

# On Windows, hide the console window
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'packages': ['numpy', 'matplotlib', 'tkinter', 'sympy'],  # Add sympy to the list
        'include_files': ['iconoCV.ico'],  # Replace with the path to your icon file
    },
}

executables = [Executable("main.py", base=base, icon='iconoCV.ico')]

setup(
    name="ProyectoCV",
    version="1.0",
    description="Diaz,Martin,Munizaga,Sanchez",
    options=options,
    executables=executables,
)
