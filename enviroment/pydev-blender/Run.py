#script to run:
#SCRIPT = "/home/t/py/other/Bevel/src/bevel.py"
SCRIPT = "/home/t/py/other/Edges/edges/edges.py"
    
#path to your org.python.pydev.debug* folder (it may have different version number, in your configuration):
PYDEVD_PATH='/home/t/.eclipse/org.eclipse.platform_3.8_155965261/plugins/org.python.pydev_3.6.0.201406232321/pysrc'

try:
    import pydev_debug as pydev
except ImportError:
    import sys
    plugin_path = '/home/t/blender-2.71-linux-glibc211-x86_64/pydev-blender/'
    sys.path.append(plugin_path)
    import pydev_debug as pydev

pydev.debug(SCRIPT, PYDEVD_PATH, trace=True)




