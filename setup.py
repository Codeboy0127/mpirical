#!/usr/bin/env python
import versioneer
import yaml

from six import string_types
from os.path import exists
from setuptools import setup


def environment_dependencies(obj, dependencies=None):
    if dependencies is None:
        dependencies = []
    if isinstance(obj, string_types):
        dependencies.append(obj.replace('=', '=='))
    elif isinstance(obj, dict):
        if 'dependencies' in obj:
            environment_dependencies(obj['dependencies'], dependencies=dependencies)
        elif 'pip' in obj:
            environment_dependencies(obj['pip'], dependencies=dependencies)
    elif isinstance(obj, list):
        for d in obj:
            environment_dependencies(d, dependencies=dependencies)
    return dependencies


with open('environment.yml') as f:
    install_requires = environment_dependencies(yaml.safe_load(f))

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''


setup(name='mpirical',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Decorate any function to make it run in parallel with MPI',
      url='https://github.com/NCAR/mpirical',
      maintainer='Kevin Paul',
      maintainer_email='kpaul@ucar.edu',
      license='https://www.apache.org/licenses/LICENSE-2.0',
      long_description=long_description,
      include_package_data=True,
      install_requires=install_requires,
      packages=['mpirical'],
      zip_safe=False)
