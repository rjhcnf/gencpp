#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['gencpp']
d['package_dir'] = {'': 'src'}
d['scripts'] = ['scripts/gen_cpp.py']
d['install_requires'] = ['genmsg']

setup(**d)
