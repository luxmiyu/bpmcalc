from cx_Freeze import setup, Executable

build_options = {
    'packages': [],
    'excludes': ["tkinter"],
    'include_files': ["resources"],
    'zip_include_packages': 'PyQt5',
}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('bpmcalc.py', base=base)
]

setup(name='template',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
