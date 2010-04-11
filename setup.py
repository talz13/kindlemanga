import glob
import sys
from distutils.core import setup
import py2exe

data_files=[('.', glob.glob(sys.prefix + '/Lib/site-packages/UnRAR2/UnRARDLL/unrar.dll'))]
options_bundle_none = dict(bundle_files = 3, dist_dir = './dist_none')
options_bundle_depends = dict(bundle_files = 2, dist_dir = './dist_dep')
options_bundle_python = dict(bundle_files = 1, dist_dir = './dist_full')

setup(script_args=['py2exe'], windows=['kindlemanga.py'], data_files=data_files, options = {'py2exe':options_bundle_none})
setup(script_args=['py2exe'], windows=['kindlemanga.py'], data_files=data_files, options = {'py2exe':options_bundle_depends})
setup(script_args=['py2exe'], windows=['kindlemanga.py'], data_files=data_files, options = {'py2exe':options_bundle_python})