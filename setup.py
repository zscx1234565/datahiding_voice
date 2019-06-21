from cx_Freeze import setup, Executable
import sys
import os.path


os.environ['TCL_LIBRARY'] = r'D:\ANACONDA\ANACONDA\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\ANACONDA\ANACONDA\tcl\tk8.6'
base = 'Win32GUI' if sys.platform=='win32' else None
includes = [r"queue",r"idna.idnadata"]
include_files = [r"D:\ANACONDA\ANACONDA\DLLs\tcl86t.dll",
                 r"D:\ANACONDA\ANACONDA\DLLs\tk86t.dll"]
executables = [
    Executable('yinpin_inhi_act.py', targetName="ACT.exe",base=base)
]

setup(name='qk',
      version = '1.0',
      description = 'seu qiangke',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=executables)
