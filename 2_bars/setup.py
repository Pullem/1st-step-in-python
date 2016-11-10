# I'm not shure, but i believe, i don't need this for my learning - Gerd

import sys
from cx_Freeze import setup, Executable

includefiles = ['.\..\..\Tools\WindowsIcons-master\WindowsPhone\dark\/appbar.close.png']

setup(
	name = "hatefulworld",
	version = "0.1",
	description = "I wish programming was this easy",
	options = {'build_exe': {'include_files':includefiles}}, 
	executables = [Executable("bars.py", base = "Win32GUI")])
