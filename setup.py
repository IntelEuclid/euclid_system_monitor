from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup


setup(
	name='system_monitor',
    version='1.0.0',
    packages=['system_monitor'],
    package_dir={'': '/intel/euclid/euclid_ws/src/system_nodes/'}
)


