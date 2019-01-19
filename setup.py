#!/usr/bin/env python
import versioneer

from setuptools import setup


def read_requires(filename):
    requires = []
    with open(filename) as f:
        for line in f:
            if line.strip()[:1] != '-':
                requires.append(line)
    return requires


setup_requires = ['versioneer']
install_requires = read_requires('requirements/production.txt')
extras_require = {'dev': read_requires('requirements/development.txt')}

setup(name='mpirical',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Decorate any function to make it run in parallel with MPI',
      url='https://github.com/NCAR/mpirical',
      maintainer='Kevin Paul',
      maintainer_email='kpaul@ucar.edu',
      license='https://www.apache.org/licenses/LICENSE-2.0',
      include_package_data=True,
      setup_requires=setup_requires,
      install_requires=install_requires,
      extras_require=extras_require,
      packages=['mpirical'],
      zip_safe=False)
