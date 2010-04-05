import glob
import sys
from distutils.core import setup
import py2exe

data_files=[('.', glob.glob(sys.prefix + '/Lib/site-packages/UnRAR2/UnRARDLL/unrar.dll')),
('gui', glob.glob('gui/*.bmp'))]

setup(script_args=['py2exe'], windows=['kindlemanga.py'], data_files=data_files,)
